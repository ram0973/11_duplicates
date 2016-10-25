# -*- coding: utf-8 -*-
from collections import defaultdict
import os
import sys
import argparse


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def find_duplicates_in(folder) -> list:
    """
    Поиск дубликатов файлов в папке.
    Дубликатами считаются файлы одного размера и названия
    :param folder: путь к папке
    :return: список с полными именами файлов - дубликатов
    """
    duplicates = defaultdict(list)
    for directory, sub_dirs, files in os.walk(folder):
        for file_name in files:
            path = os.path.join(directory, file_name)
            size = os.path.getsize(path)
            duplicates[file_name+str(size)].append(path)
    duplicates = list(filter(lambda x: len(x) > 1, duplicates.values()))
    return sorted([item for sub_list in duplicates for item in sub_list])


if __name__ == '__main__':

    load_win_unicode_console()

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='Введите путь к папке')
    folder_path = parser.parse_args().dir

    if not folder_path:
        parser.print_help()
        exit(1)

    try:
        duplicate_files = find_duplicates_in(folder_path)
    except OSError as error:
        print('Ошибка: %s в файле: %s' % (error.strerror, error.filename))
        exit(1)

    print('\nСписок дубликатов в папке %s' % folder_path)

    for duplicate_file in duplicate_files:
        print(duplicate_file)
