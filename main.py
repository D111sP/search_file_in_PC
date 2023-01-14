import array
import os
import time
import psutil

PATH = "C:\\"

def search_file(name_path, x, level = 0):
    list_item = os.listdir(name_path)  # получаем список папок и файлов в указанной директории
    if x in list_item:
        print('\t'*level + name_path + '\\' + x)
    for item in list_item:
        try:
            if os.path.isdir(name_path + '\\' + item):
                search_file(name_path + '\\' + item, x, level + 1)
        except PermissionError:  # обработка исключения прав доступа
            continue

x = input("Что ишиете?")
PATH = "C:\\"


search_file(PATH, x)


