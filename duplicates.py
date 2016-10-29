# -*- coding: utf-8 -*-
from collections import defaultdict
import os
import sys
import argparse
from contextlib import suppress


def enable_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def find_duplicates_in(folder: str) -> list:
    """
    Поиск дубликатов файлов в папке.
    Дубликатами считаются файлы одного размера и названия
    :param folder: путь к папке
    :return: список с полными именами файлов - дубликатов
    """
    duplicates = defaultdict(list)

    #  если в огромной папке система не может найти 1+ файл, который сама же и
    #  видит в списке файлов, но не находит из-за длинного имени, пропустим их
    #  ведь нам кровь из носу нужны дубликаты
    #  но как тут ругнуться на этот файл, я не знаю...

    with suppress(FileNotFoundError):
        for directory, sub_dirs, files in os.walk(folder):
            for file_name in files:
                path = os.path.join(directory, file_name)
                size = os.path.getsize(path)
                duplicates[file_name+str(size)].append(path)

    duplicates = list(filter(lambda x: len(x) > 1, duplicates.values()))
    return [item for sub_list in duplicates for item in sub_list]
    #  можно и return itertools.chain.from_iterable(duplicates)


if __name__ == '__main__':

    enable_win_unicode_console()

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
