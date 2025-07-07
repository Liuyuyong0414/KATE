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
from configs import add_args, set_seed, set_dist


def pre_train(args, logger):
    logger.info(f"[pre-train] begin pre-train.....")
    task = args.edit

    logger.info(f"[pre-train] task:{task}")
    logger.info('*' * 100)
    logger.info('[pre-train] Initializing pre-training environments')

    logger.info('-' * 100)
    logger.info('[pre-train] Building model')
    config, model, tokenizer = build_or_load_gen_model(args)

    model.to(args.device)

    train_examples, train_dataset = pre_load_and_cache_gen_data(args, args.train_filename, tokenizer)
    train_sampler = RandomSampler(train_dataset)
    train_dataloader = DataLoader(train_dataset, sampler=train_sampler, batch_size=args.pre_train_batch_size, num_workers=4, pin_memory=True)

    no_decay = ['bias', 'LayerNorm.weight']
    optimizer_grouped_parameters = [
        {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': args.weight_decay},
        {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
    ]
    optimizer = AdamW(optimizer_grouped_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
    num_train_optimization_steps = args.num_pre_train_epochs * len(train_dataloader)
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=args.warmup_steps, num_training_steps=num_train_optimization_steps)

    train_example_num = len(train_dataset)
    logger.info("[pre-train] ***** Running training *****")
    logger.info("[pre-train]   Num examples = %d", train_example_num)
    logger.info("[pre-train]   Batch size = %d", args.pre_train_batch_size)
    logger.info("[pre-train]   Batch num = %d", math.ceil(train_example_num / args.pre_train_batch_size))
    logger.info("[pre-train]   Num epoch = %d", args.num_pre_train_epochs)

    for cur_epoch in range(args.start_epoch, int(args.num_pre_train_epochs)):
        bar = tqdm(train_dataloader, total=len(train_dataloader), ncols=100, desc="Training")
        nb_tr_steps, tr_loss = 0, 0
        model.train()
        for step, batch in enumerate(bar):
            batch = tuple(t.to(args.device) for t in batch)
            source_ids, source_mask, target_ids, target_mask = batch

            if args.model_type == 'roberta':
                loss, _, _ = model(source_ids=source_ids, source_mask=source_mask, target_ids=target_ids, target_mask=target_mask)
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

        logger.info("[pre-train] ***** CUDA.empty_cache() *****")
        torch.cuda.empty_cache()
    return config, model, tokenizer
