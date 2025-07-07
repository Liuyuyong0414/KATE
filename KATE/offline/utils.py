from _utils import *
warnings.filterwarnings("ignore")
# JAVA_LANGUAGE = Language(
#     TREESITTER_LANG_SO,
#     "java",
# )
# JAVA_LANGUAGE = Language(tsjava.language())
# parser = Parser()
# parser.set_language(JAVA_LANGUAGE)
logger = logging.getLogger(__name__)


def save_pickle(data, path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)


def read_pickle(path):
    with open(path, 'rb') as f:
        examples = pickle.load(f)
    return examples


def filter_code(codes):
    codes = codes.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    codes = re.sub(' +', ' ', codes)
    return codes


def load_and_cache_gen_data(args, filename, tokenizer):
    examples = read_examples(filename)
    # calc_stats(examples, tokenizer)

    features = []
    tasks = args.edit.split(",")
    for example_index, example in enumerate(tqdm(examples, total=len(examples), desc="InputFeatures", ncols=100)):
        if args.use_best_commit:
            commit_message = "[CMG] " + example.best_commit_message
        else:
            commit_message = "[CMG] " + example.commit_message
        public_information = " ".join(("DEPENDENCY_ADD_FIELD " + example.dependency + " " + example.field).split())
        edit = " ".join(("[EDIT_SEQ] " + " ".join(example.edit_seq)).split())
        ast_edit = " ".join(("[AST_EDIT_SEQ] " + example.ast_edit_seq.replace("[+]", "+").replace("[-]", "-").replace("[/]", " ")).split())
        test_src = "[TEST_SRC] " + example.test_src
        test_tgt = example.test_tgt
        refer_test_src = "[REFER_TEST_SRC] " + example.refer_test_src
        refer_test_tgt = "[REFER_TEST_TGT] " + example.refer_test_tgt

        encode_edit = tokenizer(edit, max_length=args.max_edit_seq_length, truncation=True, padding='max_length', return_tensors="pt")
        encode_ast_edit = tokenizer(ast_edit, max_length=args.max_ast_edit_seq_length, truncation=True, padding='max_length', return_tensors="pt")
        edit_ids = []
        edit_mask = []
        for task in tasks:
            if task == "edit":
                edit_ids += encode_edit['input_ids'][0].tolist()
                edit_mask += encode_edit['attention_mask'][0].tolist()
            elif task == "ast":
                edit_ids += encode_ast_edit['input_ids'][0].tolist()
                edit_mask += encode_ast_edit['attention_mask'][0].tolist()
            else:
                raise ValueError("edit 参数不对！")

        encode_commit_message = tokenizer(commit_message, max_length=args.max_commit_message_length, truncation=True, padding='max_length', return_tensors="pt")
        encide_public_information = tokenizer(public_information, max_length=args.max_dependency_field_length, truncation=True, padding='max_length', return_tensors="pt")
        encode_test_src = tokenizer(test_src, max_length=args.max_test_src_length, truncation=True, padding='max_length', return_tensors="pt")
        encode_test_tgt = tokenizer(test_tgt, max_length=args.max_test_tgt_length, truncation=True, padding='max_length', return_tensors="pt")
        encode_refer_test_src = tokenizer(refer_test_src, max_length=args.max_refer_test_src_length, truncation=True, padding='max_length', return_tensors="pt")
        encode_refer_test_tgt = tokenizer(refer_test_tgt, max_length=args.max_refer_test_tgt_length, truncation=True, padding='max_length', return_tensors="pt")

        source_ids = []
        source_mask = []

        if args.use_commit:
            source_ids = encode_commit_message['input_ids'][0].tolist()
            source_mask = encode_commit_message['attention_mask'][0].tolist()
        if args.use_public_information:
            source_ids += encide_public_information['input_ids'][0].tolist()
            source_mask += encide_public_information['attention_mask'][0].tolist()
        source_ids += edit_ids + encode_test_src['input_ids'][0].tolist()
        source_mask += edit_mask + encode_test_src['attention_mask'][0].tolist()

        if args.use_retrieval:
            source_ids += encode_refer_test_src['input_ids'][0].tolist() + encode_refer_test_tgt['input_ids'][0].tolist()
            source_mask += encode_refer_test_src['attention_mask'][0].tolist() + encode_refer_test_tgt['attention_mask'][0].tolist()

        features.append(
            InputFeatures(
                example_index,
                source_ids,
                encode_test_tgt['input_ids'][0].tolist(),
                source_mask,
                encode_test_tgt['attention_mask'][0].tolist()
            )
        )
    return examples, GenDataset(features)


def pre_load_and_cache_gen_data(args, filename, tokenizer):
    examples = read_examples(filename)
    features = []

    tasks = args.edit.split(",")
    for example_index, example in enumerate(tqdm(examples, total=len(examples), desc="InputFeatures", ncols=100)):
        commit_message = example.commit_message
        source_ids = []
        source_mask = []
        target_ids = []
        target_mask = []

        for task in tasks:
            if task == "edit" or task == "diff":
                if task == "edit":
                    edit_seq = example.edit_seq
                elif task == "diff":
                    edit_seq = example.diff
                target_edit_seq = " ".join(" ".join(edit_seq).split())
                mask_number = math.ceil(len(edit_seq) * args.mask_ratio)
                random_numbers = random.sample(range(len(edit_seq)), mask_number)
                for i in random_numbers:
                    edit_seq[i] = list(edit_seq[i])  
                    edit_seq[i][0] = tokenizer.mask_token  
                    edit_seq[i] = ''.join(edit_seq[i])  
                source_edit_seq = " ".join(" ".join(edit_seq).split())
                encode_source_edit_seq = tokenizer(source_edit_seq, max_length=args.max_edit_seq_length, truncation=True, padding='max_length', return_tensors="pt")
                encode_target_edit_seq = tokenizer(target_edit_seq, max_length=args.max_edit_seq_length, truncation=True, padding='max_length', return_tensors="pt")
                source_ids += encode_source_edit_seq['input_ids'][0].tolist()
                source_mask += encode_source_edit_seq['attention_mask'][0].tolist()
                target_ids += encode_target_edit_seq['input_ids'][0].tolist()
                target_mask += encode_target_edit_seq['attention_mask'][0].tolist()
            elif task == "ast" or task == "ast_up":
                if task == "ast":
                    edit_seq = example.ast_edit_seq
                if task == "ast_up":
                    edit_seq = example.ast_edit_seq_up_to_down
                target_edit_seq = " ".join(edit_seq.split())
                edit_seq = edit_seq.split(" ")
                pos = []
                label_map = {"[+]": "+", "[-]": "-", "[/]": " ", }
                for idx, item in enumerate(edit_seq):
                    if item in label_map.keys():
                        edit_seq[idx] = label_map[item]
                        pos.append(idx)
                mask_number = math.ceil(len(pos) * args.mask_ratio)
                random_numbers = random.sample(pos, mask_number)
                for i in random_numbers:
                    edit_seq[i] = tokenizer.mask_token
                source_edit_seq = " ".join(" ".join(edit_seq).split())
                encode_source_edit_seq = tokenizer(source_edit_seq, max_length=args.max_ast_edit_seq_length, truncation=True, padding='max_length', return_tensors="pt")
                encode_target_edit_seq = tokenizer(target_edit_seq, max_length=args.max_ast_edit_seq_length, truncation=True, padding='max_length', return_tensors="pt")
                source_ids += encode_source_edit_seq['input_ids'][0].tolist()
                source_mask += encode_source_edit_seq['attention_mask'][0].tolist()
                target_ids += encode_target_edit_seq['input_ids'][0].tolist()
                target_mask += encode_target_edit_seq['attention_mask'][0].tolist()
            else:
                raise ValueError("edit 参数不对！")

        features.append(
            InputFeatures(
                example_index,
                source_ids,
                target_ids,
                source_mask,
                target_mask
            )
        )
    return examples, GenDataset(features)


class GenDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i):
        return (
            torch.tensor(self.data[i].source_ids),
            torch.tensor(self.data[i].source_mask),
            torch.tensor(self.data[i].target_ids),
            torch.tensor(self.data[i].target_mask))


class InputFeatures(object):
    """A single training/test features for a example."""

    def __init__(self,
                 example_id,
                 source_ids,
                 target_ids,
                 source_mask,
                 target_mask,
                 ):
        self.example_id = example_id
        self.source_ids = source_ids
        self.target_ids = target_ids
        self.source_mask = source_mask
        self.target_mask = target_mask


class Example(object):
    def __init__(self,
                 idx,
                 commit_message,
                 best_commit_message,
                 diff,
                 edit_seq,
                 ast_edit_seq,
                 dependency,
                 field,
                 test_src,
                 test_tgt,
                 refer_test_src,
                 refer_test_tgt,
                 repo_name,
                 commit,
                 refer_repo_name,
                 refer_commit
                 ):
        self.idx = idx
        self.commit_message = commit_message
        self.best_commit_message = best_commit_message
        self.diff = diff
        self.edit_seq = edit_seq
        self.ast_edit_seq = ast_edit_seq
        self.dependency = dependency
        self.field = field
        self.test_src = test_src
        self.test_tgt = test_tgt
        self.refer_test_src = refer_test_src
        self.refer_test_tgt = refer_test_tgt
        self.repo_name = repo_name
        self.commit = commit
        self.refer_repo_name = refer_repo_name
        self.refer_commit = refer_commit


def read_jsonl(path):
    data = []
    with open(path, 'r', encoding='utf-8') as jsonl_file:
        for line in jsonl_file:
            item = json.loads(line.strip())
            data.append(item)
    return data


def return_the_first_to_end(edit_seqs):
    start = -1
    end = -1
    for idx, line in enumerate(edit_seqs):
        if line.startswith('+') or line.startswith('-'):
            if start == -1:
                start = idx
            end = idx
    if start != -1 and end != -1 and start <= end:
        return [i.strip() for i in edit_seqs[start:end + 1]]
    else:
        raise ValueError("edit seq not have + or -???")


def read_examples(filename):
    examples = []
    idx = 0
    data = read_jsonl(filename)
    for line in data:
        examples.append(
            Example(
                idx=idx,
                commit_message=line['commit_message'],
                best_commit_message=line['best_commit_message'],
                diff=line['diff'],
                edit_seq=line['edit_seq'],
                ast_edit_seq=line['ast_edit_seq'],
                dependency=line['dependency'],
                field=line['field'],
                test_src=line['test_src'],
                # test_tgt=filter_code(line['test_tgt']),
                test_tgt=line['test_tgt'],
                refer_test_src=line['refer_test_src'],
                refer_test_tgt=line['refer_test_tgt'],
                repo_name=line['repo_name_1'],
                commit=line['commit_1'],
                refer_repo_name=line['repo_name_2'],
                refer_commit=line['commit_2']
            )
        )
        idx += 1
    return examples


def calc_stats(examples, tokenizer=None):
    avg_cmg_len_tokenize = []
    avg_es_len_tokenize = []
    avg_aes_len_tokenize = []
    avg_df_len_tokenize = []
    avg_ts_len_tokenize = []
    avg_tt_len_tokenize = []
    avg_rts_len_tokenize = []
    avg_rtt_len_tokenize = []
    for ex in tqdm(examples, desc="calc_stats", ncols=100):

        avg_cmg_len_tokenize.append(len(tokenizer.tokenize(ex.commit_message)))
        avg_es_len_tokenize.append(len(tokenizer.tokenize(" ".join(ex.edit_seq))))
        avg_aes_len_tokenize.append(len(tokenizer.tokenize(ex.ast_edit_seq)))
        avg_df_len_tokenize.append(len(tokenizer.tokenize(ex.dependency + ex.field)))
        avg_ts_len_tokenize.append(len(tokenizer.tokenize(ex.test_src)))
        avg_tt_len_tokenize.append(len(tokenizer.tokenize(ex.test_tgt)))
        avg_rts_len_tokenize.append(len(tokenizer.tokenize(ex.refer_test_src)))
        avg_rtt_len_tokenize.append(len(tokenizer.tokenize(ex.refer_test_tgt)))

    df = pd.DataFrame({
        'avg_cmg_len_tokenize': avg_cmg_len_tokenize,
        'avg_es_len_tokenize': avg_es_len_tokenize,
        'avg_aes_len_tokenize': avg_aes_len_tokenize,
        'avg_df_len_tokenize': avg_df_len_tokenize,
        'avg_ts_len_tokenize': avg_ts_len_tokenize,
        'avg_tt_len_tokenize': avg_tt_len_tokenize,
        'avg_rts_len_tokenize': avg_rts_len_tokenize,
        'avg_rtt_len_tokenize': avg_rtt_len_tokenize
    })
    # df.to_csv('tokenize_lengths.csv', index=False)

    logger.info("[TOKENIZE] avg cmg len: %d, max cmg len: %d", np.mean(avg_cmg_len_tokenize), max(avg_cmg_len_tokenize))
    logger.info("[TOKENIZE] avg es len: %d, max es len: %d", np.mean(avg_es_len_tokenize), max(avg_es_len_tokenize))
    logger.info("[TOKENIZE] avg aes len: %d, max aes len: %d", np.mean(avg_aes_len_tokenize), max(avg_aes_len_tokenize))
    logger.info("[TOKENIZE] avg aes_up len: %d, max aes_up len: %d", np.mean(avg_df_len_tokenize), max(avg_df_len_tokenize))
    logger.info("[TOKENIZE] avg ts len: %d, max ts len: %d", np.mean(avg_ts_len_tokenize), max(avg_ts_len_tokenize))
    logger.info("[TOKENIZE] avg tt len: %d, max tt len: %d", np.mean(avg_tt_len_tokenize), max(avg_tt_len_tokenize))
    logger.info("[TOKENIZE] avg rts len: %d, max rts len: %d", np.mean(avg_rts_len_tokenize), max(avg_rts_len_tokenize))
    logger.info("[TOKENIZE] avg rtt len: %d, max rtt len: %d", np.mean(avg_rtt_len_tokenize), max(avg_rtt_len_tokenize))


def get_elapse_time(t0):
    elapse_time = time.time() - t0
    if elapse_time > 3600:
        hour = int(elapse_time // 3600)
        minute = int((elapse_time % 3600) // 60)
        return "{}h{}m".format(hour, minute)
    else:
        minute = int((elapse_time % 3600) // 60)
        return "{}m".format(minute)


def cal_codebleu(prediction, reference):
    a, b, c, d, e = [], [], [], [], []
    for (ref, pred) in zip(reference, prediction):
        # prediction = "def add ( a , b ) :\n return a + b"
        # reference = "def sum ( first , second ) :\n return second + first"
        result = calc_codebleu([ref.test_tgt], [pred], lang="java", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
        a.append(result["codebleu"] * 100)
        b.append(result["ngram_match_score"] * 100)
        c.append(result["weighted_ngram_match_score"] * 100)
        d.append(result["syntax_match_score"] * 100)
        e.append(result["dataflow_match_score"] * 100)
    return a, b, c, d, e


def find_comments(node):
    if "comment" in node.type:
        yield node.start_byte, node.end_byte
    else:
        for child in node.children:
            yield from find_comments(child)


# def get_code_without_comments(code_str: str) -> str:
#     code_bytes = code_str.encode()
#     tree = parser.parse(code_bytes)
#     comments = list(find_comments(tree.root_node))
#     res_bytes = b""
#     start = 0
#     for comment in comments:
#         res_bytes += code_bytes[start: comment[0]]
#         # add 1 to skip the \n
#         start = comment[1] + 1
#     res_bytes += code_bytes[start:]
#     return res_bytes.decode().strip()

def sliding_window_processing(source_ids, source_mask, target_ids, target_mask,
                              window_size=512, step_size=256, pad_token_id=0):
    device = source_ids.device
    batch_size = source_ids.size(0)

    all_source, all_source_mask = [], []
    all_target, all_target_mask = [], []
    need_avg_loss = False

    for i in range(batch_size):
        src_ids = source_ids[i]
        src_mask = source_mask[i]
        tgt_ids = target_ids[i]
        tgt_mask = target_mask[i]

        seq_len = src_ids.size(0)

        if seq_len <= window_size:
            all_source.append(src_ids.unsqueeze(0))
            all_source_mask.append(src_mask.unsqueeze(0))
            all_target.append(tgt_ids.unsqueeze(0))
            all_target_mask.append(tgt_mask.unsqueeze(0))
        else:
            need_avg_loss = True
            start_indices = list(range(0, seq_len - window_size + 1, step_size))

            for start in start_indices:
                end = start + window_size
                window_src = src_ids[start:end]
                window_mask = src_mask[start:end]

                all_source.append(window_src.unsqueeze(0))
                all_source_mask.append(window_mask.unsqueeze(0))
                all_target.append(tgt_ids.unsqueeze(0))
                all_target_mask.append(tgt_mask.unsqueeze(0))

            # 补最后一块（防止信息丢失）
            if (seq_len - window_size) not in start_indices:
                window_src = src_ids[-window_size:]
                window_mask = src_mask[-window_size:]
                all_source.append(window_src.unsqueeze(0))
                all_source_mask.append(window_mask.unsqueeze(0))
                all_target.append(tgt_ids.unsqueeze(0))
                all_target_mask.append(tgt_mask.unsqueeze(0))

    new_source_ids = torch.cat(all_source, dim=0).to(device)
    new_source_mask = torch.cat(all_source_mask, dim=0).to(device)
    new_target_ids = torch.cat(all_target, dim=0).to(device)
    new_target_mask = torch.cat(all_target_mask, dim=0).to(device)

    return new_source_ids, new_source_mask, new_target_ids, new_target_mask, need_avg_loss


def sliding_window_generate(model, source_ids, source_mask,
                            window_size=512, step_size=256,
                            max_gen_length=512):
    """
    滑动窗口生成函数
    参数:
        model: 已加载的生成模型
        source_ids: 输入序列 [1, seq_len] (生成阶段batch_size=1)
        source_mask: 输入掩码 [1, seq_len]
        window_size: 滑动窗口大小
        step_size: 滑动步长
        max_gen_length: 最大生成长度

    返回:
        final_output: 合并后的生成序列（token列表）
    """
    device = source_ids.device
    seq_len = source_ids.size(1)

    # 短于窗口直接生成
    if seq_len <= window_size:
        return model.generate(
            source_ids=source_ids,
            source_mask=source_mask
        )

    # 生成滑动窗口
    windows = []
    start_indices = range(0, seq_len - window_size + 1, step_size)

    # 处理最后一个可能不足的窗口
    if (seq_len - window_size) % step_size != 0:
        start_indices = list(start_indices) + [seq_len - window_size]

    # 生成每个窗口的预测
    all_outputs = []
    for start in start_indices:
        end = start + window_size
        window_ids = source_ids[:, start:end]
        window_mask = source_mask[:, start:end]

        # 生成当前窗口的输出
        with torch.no_grad():
            window_output = model(
                source_ids=window_ids,
                source_mask=window_mask
            )
        all_outputs.append(window_output.cpu().numpy())

    return merge_window_outputs(all_outputs, step_size, window_size)


def merge_window_outputs(window_outputs, step_size, window_size):
    """
    合并滑动窗口输出序列
    策略：
      - 保留每个窗口的非重叠区域；
      - 对重叠区域只保留一个来源，避免重复；
      - 优先保留后面窗口的内容（也可改为中间窗口优先）
    参数：
        window_outputs: list of list of token ids
        step_size: 滑动步长
        window_size: 窗口大小
    返回：
        final_output: list of merged token ids
    """
    if len(window_outputs) == 1:
        return window_outputs[0]

    final_output = []
    overlap_size = window_size - step_size

    for i, output in enumerate(window_outputs):
        if i == 0:
            # 第一个窗口：保留全长
            final_output.extend(output)
        else:
            # 其余窗口：跳过重叠部分的前面区域，只加后面新增部分
            final_output.extend(output[overlap_size:])

    return final_output
