# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: refer https://github.com/ThilinaRajapakse/simpletransformers
"""
import sys
from multiprocessing import cpu_count

global_args = {
    "adam_epsilon": 1e-8,
    "best_model_dir": "outputs/best_model",
    "cache_dir": "cache_dir/",
    "config": {},
    "do_lower_case": False,
    "early_stopping_consider_epochs": False,
    "early_stopping_delta": 0,
    "early_stopping_metric": "eval_loss",
    "early_stopping_metric_minimize": True,
    "early_stopping_patience": 3,
    "encoding": None,
    "eval_batch_size": 8,
    "evaluate_during_training": False,
    "evaluate_during_training_silent": True,
    "evaluate_during_training_steps": 2000,
    "evaluate_during_training_verbose": False,
    "fp16": True,
    "gradient_accumulation_steps": 1,
    "learning_rate": 4e-5,
    "local_rank": -1,
    "logging_steps": 50,
    "manual_seed": None,
    "max_grad_norm": 1.0,
    "max_seq_length": 128,
    "multiprocessing_chunksize": 500,
    "n_gpu": 1,
    "no_cache": False,
    "no_save": False,
    "num_train_epochs": 1,
    "output_dir": "outputs/",
    "overwrite_output_dir": False,
    "process_count": cpu_count() - 2 if cpu_count() > 2 else 1,
    "reprocess_input_data": True,
    "save_best_model": True,
    "save_eval_checkpoints": True,
    "save_model_every_epoch": True,
    "save_steps": 2000,
    "save_optimizer_and_scheduler": True,
    "silent": False,
    "tensorboard_dir": None,
    "train_batch_size": 8,
    "use_cached_eval_features": False,
    "use_early_stopping": False,
    "use_multiprocessing": True,
    "wandb_kwargs": {},
    "wandb_project": None,
    "warmup_ratio": 0.06,
    "warmup_steps": 0,
    "weight_decay": 0,
}

if sys.platform == "win32":
    global_args["process_count"] = min(global_args["process_count"], 61)
