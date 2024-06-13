# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS:
#  перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
#  перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
#  перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#  перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему пр

import os

import shutil

folder_path = '../test'

if os.path.isdir(folder_path):
    shutil.rmtree(folder_path)
    print('Папка удалена')
else:
    print('Папка не найдена')



print("Пункт 1")
print('-' * 100)
os.chdir("../PZ_11")
files = []


for obj in os.listdir():

    if os.path.isfile(obj):

        files.append(obj)


print(files)


print("Пункт 2")
print('-' * 100)


os.chdir("..")
os.mkdir("test")
os.mkdir("test/test1")

with open("./PZ6/Пз6.pdf", "rb") as src_file:
    with open("test/Пз6.pdf", "wb") as dst_file:
        dst_file.write(src_file.read())

with open("./PZ6/PZ_6_1.py", "r", encoding="utf-8") as src_file:
    with open("test/PZ_6_1.py", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())


with open("./pz7/PZ_7_1.py", "r", encoding="utf-8") as src_file:
    with open("test/test1/test.txt", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

sizes = []
for file in os.listdir("test"):
    if os.path.isfile(os.path.join("test", file)):
        sizes.append(os.path.getsize(os.path.join("test", file)))

print(sizes)


print("Пункт 3")
print('-' * 100)


os.chdir("./PZ_11")

shortest_filename = ""
for filename in os.listdir():
    if len(filename) < len(shortest_filename) or shortest_filename == "":
        shortest_filename = filename

print(os.path.basename(shortest_filename))


print("Пункт 4")
print('-' * 100)


pdf_folder = '../PZ6'
pdf_filename = 'Пз6.pdf'
pdf_path = os.path.join(pdf_folder, pdf_filename)

if os.path.isfile(pdf_path):
    os.startfile(pdf_path)
else:
    print("такого файла нет")


print("Пункт 5")
print('-' * 100)


os.chdir = '../test/test1'

file_path = os.path.join(os.chdir, 'test.txt')

if os.path.isfile(file_path):
    os.remove(file_path)
    print('Файл успешно удален.')
else:
    print('Файл не найден.')


print("Пункт 6")
print('-' * 100)



