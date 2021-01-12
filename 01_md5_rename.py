#!/usr/bin/env python3
import hashlib
import tqdm
import os
import shutil

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

new_root = "stage1"
os.makedirs(new_root, exist_ok=True)
for root, dirs, files in tqdm.tqdm(os.walk(".")):
    for file_path in tqdm.tqdm(files):
        ext = os.path.splitext(file_path)[1].lower()
        if ext in [".mp4", ".mkv"]:
            path = os.path.abspath(os.path.join(root, file_path))
            path_md5 = md5(path)

            new_path = os.path.abspath(os.path.join(new_root, f"{path_md5}{ext}"))

            if not os.path.exists(new_path):
                shutil.copy(path, new_path)
