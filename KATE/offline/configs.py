import random
import logging
import torch
import logging
import multiprocessing
import numpy as np
import os

logger = logging.getLogger(__name__)


def add_args(parser):
    parser.add_argument("--model_type", default="codet5", type=str, choices=['codet5', 't5', 'codegen', 'bart', 'codet5p', 'codebert', 'unixcoder', 'plbart', 'codegen'])
    parser.add_argument("--start_epoch", default=0, type=int)
    parser.add_argument("--num_train_epochs", default=100, type=int)
    parser.add_argument("--num_pre_train_epochs", default=5, type=int)
    parser.add_argument("--mask_ratio", default=0.4, type=int)
    parser.add_argument("--patience", default=3, type=int)

    # Required parameters
    parser.add_argument("--output_dir", default="output", type=str)

    # Other parameters
    parser.add_argument("--train_filename", default="", type=str)
    parser.add_argument("--dev_filename", default="", type=str)
    parser.add_argument("--test_filename", default="", type=str)

    parser.add_argument("--max_commit_message_length", default=32, type=int)
    parser.add_argument("--max_dependency_field_length", default=128, type=int)
    parser.add_argument("--max_ast_edit_seq_length", default=384, type=int)
    parser.add_argument("--max_edit_seq_length", default=256, type=int)
    parser.add_argument("--max_test_src_length", default=512, type=int)
    parser.add_argument("--max_test_tgt_length", default=512, type=int)
    parser.add_argument("--max_refer_test_src_length", default=400, type=int)
    parser.add_argument("--max_refer_test_tgt_length", default=400, type=int)


    parser.add_argument("--do_pre_train", action="store_true", help="Whether to run pretrain.")
    parser.add_argument("--do_train", action="store_true", help="Whether to run training.")
    parser.add_argument("--do_eval", action="store_true", help="Whether to run evaluation.")
    parser.add_argument("--do_test", action="store_true", help="Whether to run testing.")
    parser.add_argument("--use_best_commit", action="store_true", help="Whether to use_best_commit.")

    parser.add_argument("--device", type=str, default=None, help="Device to use for training (e.g., 'cuda' or 'cpu')")
    parser.add_argument("--train_batch_size", default=1, type=int, help="Batch size per GPU/CPU for training.")
    parser.add_argument("--pre_train_batch_size", default=5, type=int, help="Batch size per GPU/CPU for training.")
    parser.add_argument("--eval_batch_size", default=5, type=int, help="Batch size per GPU/CPU for evaluation.")

    parser.add_argument('--gradient_accumulation_steps', type=int, default=1, help="Number of updates steps to accumulate before performing a backward/update pass.")
    parser.add_argument("--learning_rate", default=5e-5, type=float, help="The initial learning rate for Adam.")
    parser.add_argument("--beam_size", default=5, type=int, help="beam size for beam search")
    parser.add_argument("--weight_decay", default=0.01, type=float, help="Weight decay if we apply some.")
    parser.add_argument("--adam_epsilon", default=1e-8, type=float, help="Epsilon for Adam optimizer.")

    parser.add_argument("--warmup_steps", default=100, type=int, help="Linear warmup over warmup_steps.")
    parser.add_argument('--seed', type=int, default=1234, help="random seed for initialization")
    parser.add_argument('--gpu', type=int, default=0, help="choose gpu")
    parser.add_argument('--use_retrieval', type=int, default=1, help="weather retrieval")
    parser.add_argument('--use_commit', type=int, default=1, help="weather use commit message")
    parser.add_argument('--use_public_information', type=int, default=1, help="weather use public information")
    parser.add_argument('--edit', type=str, default='ast', help="weather use edit")
    args = parser.parse_args()
    parser.add_argument("--base_model", default=f"./model/{args.model_type}", type=str)
    parser.add_argument("--res_dir", default=f"{args.output_dir}/res_dir/", type=str)
    args = parser.parse_args()

    os.makedirs(args.res_dir, exist_ok=True)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.INFO)
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler(f"{args.output_dir}/logfile.log", mode='w')  # 可以修改 'w' 为 'a' 来追加日志
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S'
    ))
    logger.addHandler(file_handler)
    return args, logger


def set_dist(args):
    if torch.cuda.is_available():
        args.device = f"cuda:{args.gpu}"
    else:
        args.device = "cpu"


def set_seed(args):
    """set random seed."""
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed_all(args.seed)
    torch.backends.cudnn.deterministic = True
