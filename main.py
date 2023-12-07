import pandas as pd
import json
import ipdb
import os
from glob import glob

dir_path = "./train"
parquet_files = glob(os.path.join(dir_path, "*", "*.parquet"))
json_files = glob(os.path.join(dir_path, "*", "*.json"))


for parquet_file_name, json_file_name in zip(parquet_files, json_files):
    df = pd.read_parquet(parquet_file_name)

    with open(json_file_name) as f:
        json_data = json.load(f)

    # print(df.head())
    # print(json_data)
    df.to_csv("data_sample.csv", index=False)
    break
