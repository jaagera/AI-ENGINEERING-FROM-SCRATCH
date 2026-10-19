from datasets import load_dataset

ds = load_dataset("glue", "mrpc")
print(ds)                      # shows the train / validation / test splits and sizes
print(ds["train"][:5])         # first 5 examples
print(ds["train"].column_names)

import time
from datasets import load_dataset

def stream_count(seconds=10):
    ds = load_dataset("glue", "mrpc", split="train", streaming=True)
    start = time.time()
    count = 0
    for example in ds:
        count += 1
        if time.time() > start + seconds:
            break
    return count, time.time() - start

print(stream_count())
print(stream_count())   # run twice and compare

import os
from datasets import load_dataset

ds = load_dataset("glue", "mrpc", split="train")

ds.to_csv("mrpc_train.csv")
ds.to_parquet("mrpc_train.parquet")

for f in ["mrpc_train.csv", "mrpc_train.parquet"]:
    print(f, os.path.getsize(f), "bytes")

# Load the Parquet file back
back = load_dataset("parquet", data_files="mrpc_train.parquet", split="train")

print(len(ds), len(back))
assert len(ds) == len(back), "row count changed!"

from datasets import load_dataset

SEED = 42

def make_splits(seed=SEED):
    ds = load_dataset("glue", "mrpc", split="train")

    first = ds.train_test_split(test_size=0.3, seed=seed)   # 70% / 30%
    train = first["train"]

    rest = first["test"].train_test_split(test_size=0.5, seed=seed)  # halve the 30%
    val, test = rest["train"], rest["test"]
    return ds, train, val, test

ds, train, val, test = make_splits()
print(len(train), len(val), len(test))     # roughly 70% / 15% / 15%
assert len(train) + len(val) + len(test) == len(ds)

# Reproducibility check: same seed, same first row in each split
_, train2, val2, test2 = make_splits()
assert train[0] == train2[0]
assert val[0] == val2[0]
assert test[0] == test2[0]
print("Splits are reproducible")