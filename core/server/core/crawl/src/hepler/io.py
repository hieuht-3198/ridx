import os
from os import walk


def make_dir(dir_path):
    try:
        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
    except:
        pass

def get_all_files(dir_path):
    return next(walk(dir_path), (None, None, []))[2]