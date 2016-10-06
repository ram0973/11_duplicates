# -*- coding: utf-8 -*-
import os
import sys
import argparse


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def get_named_argument(arg_name: str) -> str:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument('--' + arg_name)
        return getattr(parser.parse_args(sys.argv[1:]), arg_name)
    else:
        print('Введите параметр в формате --%s Значение' % arg_name)
        exit(1)


def find_duplicates(root_dir: str):
    duplicates = {}
    for dir, subdirs, files in os.walk(root_dir):
        for filename in files:
            path = os.path.join(dir, filename)
            size = os.path.getsize(path)
            if filename+str(size) not in duplicates:
                duplicates[filename+str(size)] = [path]
            else:
                duplicates[filename+str(size)].append(path)
    duplicates = list(filter(lambda x: len(x) > 1, duplicates.values()))
    return sorted([item for sublist in duplicates for item in sublist])


if __name__ == '__main__':

    load_win_unicode_console()

    root_dir = get_named_argument('dir')

    duplicates = find_duplicates(root_dir)

    for el in duplicates:
        print(el)
