# -*- coding: utf-8 -*-
import os
import sys


def are_files_duplicates(file_path1, file_path_2):
    if os.path.getsize(file_path1) == os.path.getsize(file_path_2) and \
       os.path.split(file_path1)[1] == os.path.split(file_path_2)[1]:
            return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        print('Введите имя папки как аргумент')
        exit()

    file_names = []
    for dir, subdirs, files in os.walk(root_dir):
        for filename in files:
            path = os.path.join(dir, filename)
            file_names.append(path)

    #
    duplicates = set()
    for el1 in file_names:
        for el2 in file_names:
            if el1 != el2 and are_files_duplicates(el1, el2):
                duplicates.add(el1)
                duplicates.add(el2)

    for el in (sorted(duplicates)):
        print(el)
