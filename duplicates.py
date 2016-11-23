# -*- coding: utf-8 -*-
from collections import defaultdict
import os
import argparse
from contextlib import suppress
import itertools


def find_duplicates_in(folder: str) -> list:
    duplicates = defaultdict(list)
    with suppress(FileNotFoundError):
        for directory, sub_dirs, files in os.walk(folder):
            for file_name in files:
                path = os.path.join(directory, file_name)
                size = os.path.getsize(path)
                duplicates[file_name+str(size)].append(path)
    duplicates = list(filter(lambda x: len(x) > 1, duplicates.values()))
    return itertools.chain.from_iterable(duplicates)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='Enter folder path', required=True)
    folder_path = parser.parse_args().dir
    duplicate_files = find_duplicates_in(folder_path)
    print('\nDuplicates list in folder %s' % folder_path)
    for duplicate_file in duplicate_files:
        print(duplicate_file)
