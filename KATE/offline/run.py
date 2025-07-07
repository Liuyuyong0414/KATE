import os
import torch
import logging
import argparse
import math
import builtins
import numpy as np
from tqdm import tqdm
import multiprocessing
import time
# import pandas as pd
from torch.utils.data import DataLoader, SequentialSampler, RandomSampler
from torch.utils.data.distributed import DistributedSampler
from transformers import AdamW, get_linear_schedule_with_warmup
from models import build_or_load_gen_model
from evaluator import smooth_bleu
from evaluator.CodeBLEU import calc_code_bleu
from evaluator.bleu import _bleu
from utils import *
from pre_train import pre_train
from configs import add_args, set_seed, set_dist

os.environ["TOKENIZERS_PARALLELISM"] = "false"


def eval_ppl_epoch(args, eval_dataset, model, tokenizer):
    eval_sampler = SequentialSampler(eval_dataset)
    eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args.eval_batch_size, num_workers=4, pin_memory=True)
    logger.info("  " + "***** Running ppl evaluation *****")
    logger.info("  Num examples = %d", len(eval_dataset))
    logger.info("  Batch size = %d", args.eval_batch_size)

    model.eval()
    eval_loss, batch_num = 0, 0
    for batch in tqdm(eval_dataloader, total=len(eval_dataloader), desc="Eval ppl", ncols=100):
        batch = tuple(t.to(args.device) for t in batch)
        source_ids, source_mask, target_ids, target_mask = batch
        with torch.no_grad():
            if args.model_type in ['roberta', 'codebert']:
                # original_source = source_ids
                # original_source_mask = source_mask
                # original_target = target_ids
                # original_target_mask = target_mask
                # processed_source, processed_mask, processed_target, processed_tmask, need_avg = \
                #     sliding_window_processing(original_source, original_source_mask,
                #                               original_target, original_target_mask)
                # loss, _, _ = model(
                #     source_ids=processed_source,
                #     source_mask=processed_mask,
                #     target_ids=processed_target,
                #     target_mask=processed_tmask
                # )
                # if need_avg:
                #     loss = loss / (processed_source.size(0) / original_source.size(0))

                loss, _, _ = model(source_ids=source_ids, source_mask=source_mask,
                                   target_ids=target_ids, target_mask=target_mask)
            else:
                outputs = model(input_ids=source_ids, attention_mask=source_mask, labels=target_ids, decoder_attention_mask=target_mask)
                loss = outputs.loss
        eval_loss += loss.item()
        batch_num += 1
    eval_loss = eval_loss / batch_num
    eval_ppl = round(np.exp(eval_loss), 5)
    return eval_ppl


def eval_bleu_epoch(args, eval_dataset, eval_examples, model, tokenizer, split_tag, criteria):
    # if args.model_type in ['roberta', 'codebert']:
    #     # args.eval_batch_size = 15 * args.train_batch_size
    #     args.eval_batch_size = 5 * args.train_batch_size
    args.eval_batch_size = 10

    logger.info("  ***** Running bleu evaluation on {} data*****".format(split_tag))
    logger.info("  Num examples = %d", len(eval_dataset))
    logger.info("  Batch size = %d", args.eval_batch_size)
    eval_sampler = SequentialSampler(eval_dataset)

    eval_dataloader = DataLoader(eval_dataset, sampler=eval_sampler, batch_size=args.eval_batch_size, num_workers=4, pin_memory=True)

    model.eval()
    pred_ids = []
    bleu, codebleu = 0.0, 0.0
    for batch in tqdm(eval_dataloader, total=len(eval_dataloader), ncols=100, desc="Eval bleu for {} set".format(split_tag)):
        batch = tuple(t.to(args.device) for t in batch)
        source_ids, source_mask, target_ids, target_mask = batch
        with torch.no_grad():
            if args.model_type in ['roberta', 'codebert']:
                # preds = sliding_window_generate(
                #     model=model,
                #     source_ids=source_ids,
                #     source_mask=source_mask,
                #     window_size=512,
                #     step_size=256,
                #     max_gen_length=args.max_test_tgt_length
                # )
                # top_preds = [pred[0] for pred in preds]
                preds = model(source_ids=source_ids, source_mask=source_mask)

                top_preds = [pred[0].cpu().numpy() for pred in preds]
            else:
                # preds = model.generate(input_ids=source_ids, attention_mask=source_mask, use_cache=True, num_beams=args.beam_size, max_length=args.max_test_tgt_length)
                preds = model.generate(input_ids=source_ids, attention_mask=source_mask, max_length=args.max_test_tgt_length)
                top_preds = list(preds.cpu().numpy())
            pred_ids.extend(top_preds)

    pred_nls = [tokenizer.decode(id, skip_special_tokens=True, clean_up_tokenization_spaces=False) for id in pred_ids]

    if split_tag == "dev":
        output_fn = os.path.join(args.res_dir, "dev_{}.output".format(criteria))
        gold_fn = os.path.join(args.res_dir, "dev_{}.gold".format(criteria))
    else:
        output_fn = os.path.join(args.res_dir, "test.output")
        gold_fn = os.path.join(args.res_dir, "test.gold")
    dev_accs = []
    repo = {}
    with open(output_fn, 'w', encoding="utf-8") as f, open(gold_fn, 'w', encoding="utf-8") as f1:
        for pred_nl, gold in zip(pred_nls, eval_examples):
            dev_accs.append(pred_nl.strip() == gold.test_tgt.strip())
            if gold.repo_name not in repo.keys():
                repo[gold.repo_name] = [0, 0]
            repo[gold.repo_name][int(pred_nl.strip() == gold.test_tgt.strip())] += 1
            # print(pred_nl.strip().replace('\n', '\\n'))
            f.write(pred_nl.strip().replace('\n', '\\n') + '\n')
            f1.write(gold.test_tgt.strip().replace('\n', '\\n') + '\n')
    with open(os.path.join(args.output_dir, "repo_name.json"), 'w') as f:
        json.dump(repo, f)
    bleu = round(_bleu(gold_fn, output_fn), 2)
    codebleu, ngram_match_score, weighted_ngram_match_score, syntax_match_score, dataflow_match_score = cal_codebleu(pred_nls, eval_examples)
    em = np.mean(dev_accs) * 100
    if split_tag == "test":
        with open(os.path.join(args.res_dir, "test_output_gold.json"), "w", encoding="utf-8") as f:
            for i, j, k, l in zip(eval_examples, pred_nls, dev_accs, codebleu):
                ans = {
                    "test_src": i.test_src.strip(),
                    "test_tgt": i.test_tgt.strip(),
                    "refer_test_src": i.refer_test_src.strip(),
                    "refer_test_tgt": i.refer_test_tgt.strip(),
                    "predict_test": j.strip(),
                    "repo_name": i.repo_name.strip(),
                    "commit": i.commit,
                    "refer_repo_name": i.refer_repo_name.strip(),
                    "refer_commit": i.refer_commit,
                    "acc": float(k),
                    "codebleu": float(l)
                }
                json.dump(ans, f, ensure_ascii=False)
                f.write('\n')
    result = {
        'em': em, 'bleu': bleu, 'codebleu': np.mean(codebleu),
        'ngram_match_score': np.mean(ngram_match_score), 'weighted_ngram_match_score': np.mean(weighted_ngram_match_score),
        'syntax_match_score': np.mean(syntax_match_score), 'dataflow_match_score': np.mean(dataflow_match_score)}
    logger.info("***** Eval results *****")
    for key in sorted(result.keys()):
        logger.info("  %s = %s", key, str(round(result[key], 4)))

    return result


def main():
    parser = argparse.ArgumentParser()
    args, logger = add_args(parser)
    logger.info(args)
    t0 = time.time()

    set_dist(args)
    # set_seed(args)

    fa = open(os.path.join(args.output_dir, 'summary.log'), 'a+')
    fb = open(os.path.join(args.output_dir, 'eval_summary.log'), 'a+')
    model = None
    if args.do_pre_train:
        config, model, tokenizer = pre_train(args, logger)
    if args.do_train:
        if model is None:
            config, model, tokenizer = build_or_load_gen_model(args)
            model.to(args.device)
        tokenizer.add_tokens(['[CMG]', '[DEPENDENCY_ADD_FIELD]', '[AST_EDIT_SEQ]', '[EDIT_SEQ]', '[TEST_SRC]', '[REFER_TEST_SRC]', '[REFER_TEST_TGT]'])
        if args.model_type in ['roberta', 'codebert']:
            model.encoder.resize_token_embeddings(len(tokenizer))
        else:
            model.resize_token_embeddings(len(tokenizer))

        train_examples, train_dataset = load_and_cache_gen_data(args, args.train_filename, tokenizer)
        train_sampler = RandomSampler(train_dataset)
        train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=args.train_batch_size, num_workers=4, pin_memory=True)

        no_decay = ['bias', 'LayerNorm.weight']
        optimizer_grouped_parameters = [
            {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': args.weight_decay},
            {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
        ]
        optimizer = AdamW(optimizer_grouped_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
        num_train_optimization_steps = args.num_train_epochs * len(train_dataloader)
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=args.warmup_steps, num_training_steps=num_train_optimization_steps)

        train_example_num = len(train_dataset)
        logger.info("***** Running training *****")
        logger.info("  Num examples = %d", train_example_num)
        logger.info("  Batch size = %d", args.train_batch_size)
        logger.info("  Batch num = %d", math.ceil(train_example_num / args.train_batch_size))
        logger.info("  Num epoch = %d", args.num_train_epochs)

        best_codebleu, best_em, best_codebleu_em, best_ppl = -1, -1, -1, 1e6
        not_loss_dec_cnt, not_bleu_em_inc_cnt = 0, 0

        for cur_epoch in range(args.start_epoch, int(args.num_train_epochs)):
            bar = tqdm(train_dataloader, total=len(train_dataloader), ncols=100, desc="Training")
            nb_tr_steps, tr_loss = 0, 0
            model.train()
            for step, batch in enumerate(bar):
                batch = tuple(t.to(args.device) for t in batch)
                source_ids, source_mask, target_ids, target_mask = batch
                if args.model_type in ['codebert']:
                    loss, _, _ = model(source_ids=source_ids, source_mask=source_mask,
                                       target_ids=target_ids, target_mask=target_mask)
                elif args.model_type in ['codegen']:
                    input_ids = torch.cat([source_ids, target_ids], dim=1)
                    attention_mask = torch.cat([source_mask, target_mask], dim=1)
                    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
                    loss = outputs.loss
                    print(loss)
                else:
                    outputs = model(input_ids=source_ids, attention_mask=source_mask, labels=target_ids, decoder_attention_mask=target_mask)
                    loss = outputs.loss

                if args.gradient_accumulation_steps > 1:
                    loss = loss / args.gradient_accumulation_steps
                tr_loss += loss.item()

                nb_tr_steps += 1
                loss.backward()

                if nb_tr_steps % args.gradient_accumulation_steps == 0:
                    optimizer.step()
                    optimizer.zero_grad()
                    scheduler.step()
                    train_loss = round(tr_loss * args.gradient_accumulation_steps / (nb_tr_steps + 1), 4)
                    bar.set_description("[{}] Train loss {}".format(cur_epoch, round(train_loss, 3)))

            logger.info("***** CUDA.empty_cache() *****")
            torch.cuda.empty_cache()
            if args.do_eval:
                eval_examples, eval_dataset = load_and_cache_gen_data(args, args.dev_filename, tokenizer)
                # ppl是困惑度指标
                eval_ppl = eval_ppl_epoch(args, eval_dataset, model, tokenizer)
                result = {'epoch': cur_epoch, 'eval_ppl': eval_ppl}
                for key in sorted(result.keys()):
                    logger.info("  %s = %s", key, str(result[key]))
                logger.info("  " + "*" * 20)

                # keep model
                last_output_dir = os.path.join(args.output_dir, 'checkpoint-last', str(cur_epoch))
                os.makedirs(last_output_dir, exist_ok=True)
                model_to_save = model.module if hasattr(model, 'module') else model
                output_model_file = os.path.join(last_output_dir, "pytorch_model.bin")
                torch.save(model_to_save.state_dict(), output_model_file)
                logger.info("Save the last model into %s", output_model_file)

                if eval_ppl < best_ppl:
                    not_loss_dec_cnt = 0
                    logger.info("  Best ppl:%s", eval_ppl)
                    logger.info("  " + "*" * 20)
                    fa.write("[%d] Best ppl changed into %.4f\n" % (cur_epoch, eval_ppl))
                    best_ppl = eval_ppl

                    output_dir = os.path.join(args.output_dir, 'checkpoint-best-ppl')
                    os.makedirs(output_dir, exist_ok=True)
                    model_to_save = model.module if hasattr(model, 'module') else model
                    output_model_file = os.path.join(output_dir, "pytorch_model.bin")
                    torch.save(model_to_save.state_dict(), output_model_file)
                    logger.info("Save the best ppl model into %s", output_model_file)
                else:
                    not_loss_dec_cnt += 1
                    logger.info("Ppl does not decrease for %d epochs", not_loss_dec_cnt)
                    if all([x > args.patience for x in [not_bleu_em_inc_cnt, not_loss_dec_cnt]]):
                        early_stop_str = "[%d] Early stop as not_bleu_em_inc_cnt=%d, and not_loss_dec_cnt=%d\n" % (cur_epoch, not_bleu_em_inc_cnt, not_loss_dec_cnt)
                        logger.info(early_stop_str)
                        fa.write(early_stop_str)
                        break
                # logger.info("***** CUDA.empty_cache() *****")
                torch.cuda.empty_cache()

                # val bleu
                result = eval_bleu_epoch(args, eval_dataset, eval_examples, model, tokenizer, 'dev', 'e%d' % cur_epoch)
                dev_codebleu, dev_bleu, dev_em = result['codebleu'], result['bleu'], result['em']
                fb.write("[%d] Eval codebleu+em changed into %.2f (dev_codebleu: %.2f, em: %.2f)\n" % (cur_epoch, dev_codebleu + dev_em, dev_codebleu, dev_em))
                dev_codebleu_em = dev_codebleu + dev_em
                if dev_em > best_em:
                    logger.info("  [%d] Best em: %.2f ", cur_epoch, dev_em)
                    logger.info("  " + "*" * 20)
                    best_em = dev_em
                    fa.write("[%d] Best em changed into %.2f \n" % (cur_epoch, dev_em))

                    output_dir = os.path.join(args.output_dir, 'checkpoint-best-em')
                    os.makedirs(output_dir, exist_ok=True)
                    model_to_save = model.module if hasattr(model, 'module') else model
                    output_model_file = os.path.join(output_dir, "pytorch_model.bin")
                    torch.save(model_to_save.state_dict(), output_model_file)
                    logger.info("Save the best em model into %s", output_model_file)

                if dev_codebleu > best_codebleu:
                    logger.info("  [%d] Best codebleu: %.2f ", cur_epoch, dev_codebleu)
                    logger.info("  " + "*" * 20)
                    best_codebleu = dev_codebleu
                    fa.write("[%d] Best codebleu changed into %.2f \n" % (cur_epoch, dev_codebleu))

                    output_dir = os.path.join(args.output_dir, 'checkpoint-best-codebleu')
                    os.makedirs(output_dir, exist_ok=True)
                    model_to_save = model.module if hasattr(model, 'module') else model
                    output_model_file = os.path.join(output_dir, "pytorch_model.bin")
                    torch.save(model_to_save.state_dict(), output_model_file)
                    logger.info("Save the best codebleu model into %s", output_model_file)

                if dev_codebleu_em > best_codebleu_em:
                    not_bleu_em_inc_cnt = 0
                    logger.info("  [%d] Best codebleu+em: %.2f (codebleu: %.2f, em: %.2f)", cur_epoch, dev_codebleu_em, dev_codebleu, dev_em)
                    logger.info("  " + "*" * 20)
                    best_codebleu_em = dev_codebleu_em
                    fa.write("[%d] Best codebleu+em changed into %.2f (codebleu: %.2f, em: %.2f)\n" % (cur_epoch, best_codebleu_em, dev_codebleu, dev_em))

                    output_dir = os.path.join(args.output_dir, 'checkpoint-best-codebleu-em')
                    os.makedirs(output_dir, exist_ok=True)
                    model_to_save = model.module if hasattr(model, 'module') else model
                    output_model_file = os.path.join(output_dir, "pytorch_model.bin")
                    torch.save(model_to_save.state_dict(), output_model_file)
                    logger.info("Save the best codebleu-em model into %s", output_model_file)
                else:
                    not_bleu_em_inc_cnt += 1
                    logger.info("codebleu does not increase for %d epochs", not_bleu_em_inc_cnt)
                    if all([x > args.patience for x in [not_bleu_em_inc_cnt, not_loss_dec_cnt]]):
                        stop_early_str = "[%d] Early stop as not_bleu_em_inc_cnt=%d, and not_loss_dec_cnt=%d\n" % (cur_epoch, not_bleu_em_inc_cnt, not_loss_dec_cnt)
                        logger.info(stop_early_str)
                        fa.write(stop_early_str)
                        break

            # logger.info("***** CUDA.empty_cache() *****")
            torch.cuda.empty_cache()

        logger.info("Finish training and take %s", get_elapse_time(t0))

    if args.do_test:
        if model is None:
            config, model, tokenizer = build_or_load_gen_model(args)
            model.to(args.device)
        tokenizer.add_tokens(['[CMG]', '[DEPENDENCY_ADD_FIELD]', '[AST_EDIT_SEQ]', '[EDIT_SEQ]', '[TEST_SRC]', '[REFER_TEST_SRC]', '[REFER_TEST_TGT]'])
        if args.model_type in ['roberta', 'codebert']:
            model.encoder.resize_token_embeddings(len(tokenizer))
        else:
            model.resize_token_embeddings(len(tokenizer))
        test_examples, test_dataset = load_and_cache_gen_data(args, args.test_filename, tokenizer)
        logger.info("  " + "***** Testing *****")
        logger.info("  Batch size = %d", args.eval_batch_size)
        # for criteria in ['best-codebleu', 'best-em', 'best-codebleu-em', 'best-ppl']:
        for criteria in ['best-codebleu-em']:
            file = os.path.join(args.output_dir, 'checkpoint-{}/pytorch_model.bin'.format(criteria))
            logger.info("Reload model from {}".format(file))
            model.load_state_dict(torch.load(file))
            result = eval_bleu_epoch(args, test_dataset, test_examples, model, tokenizer, 'test', criteria)
            test_codebleu, test_bleu, test_em = result['codebleu'], result['bleu'], result['em']
            result_str = "[%s] bleu-4: %.2f, em: %.4f, codebleu: %.4f\n" % (criteria, test_bleu, test_em, test_codebleu)
            logger.info(result_str)
            fa.write(result_str)


# def custom_print(*args, **kwargs):
#     if 'There is no reference data-flows' in args[0]:
#         return
#     builtins.print(*args, **kwargs)


if __name__ == "__main__":
    # builtins.print = custom_print
    main()
