# Решение задачи [№11](https://devman.org/challenges/1/) с сайта [devman.org](https://devman.org)

## Условие задачи:

Нужен скрипт, который принимает на вход папку, просматривает все файлы 
в ней (и всех подпапках и под-под-...папках) и сообщает, если находит 
дубликаты. Дубликаты – это два файла с одинаковым именем и размером.

## Системные требования

```
Python 3.5.2+
Внешний модуль win-unicode-console
Внешний модуль colorama
```

## Установка

Windows

```    
git clone https://github.com/ram0973/11_duplicates.git
cd 11_duplicates
pip install -r requirements.txt
```

Linux
```    
git clone https://github.com/ram0973/11_duplicates.git
cd 11_duplicates
pip3 install -r requirements.txt
```
    
## Описание работы
Пользователь вводит путь к папке как аргумент dir.
Пример:
 
```
python duplicates.py --dir .
```

Скрипт печатает список дубликатов файлов из заданной папки. 
    
## Запуск

Windows

python duplicates.py --dir ПутькПапке
 
Linux
 
python3 duplicates.py --dir ПутькПапке

## Лицензия

[MIT](http://opensource.org/licenses/MIT)