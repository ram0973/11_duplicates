﻿# -*- coding: utf-8 -*-
from collections import defaultdict
import os
import sys
import argparse


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    и раскрашивание символов
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
        from colorama import init
        init()  # colorama


def get_folder_path_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='Введите путь к папке')
    if parser.parse_args().dir:
        return parser.parse_args().dir
    else:
        parser.print_help()
        exit(1)


def find_duplicates_in(folder: str):
    duplicates = defaultdict(list)
    for directory, sub_dirs, files in os.walk(folder):
        for filename in files:
            path = os.path.join(directory, filename)
            size = os.path.getsize(path)
            duplicates[filename+str(size)].append(path)
    duplicates = list(filter(lambda x: len(x) > 1, duplicates.values()))
    return sorted([item for sub_list in duplicates for item in sub_list])


if __name__ == '__main__':

    load_win_unicode_console()

    folder_path = get_folder_path_argument()

    duplicates_list = find_duplicates_in(folder_path)

    for el in duplicates_list:
        print(el)
