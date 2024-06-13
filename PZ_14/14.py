#Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
#маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
#все остальные. Посчитать количество полученных строк в каждом файле

import re


with open('ip_address.txt', 'r') as f:
    lines = f.readlines()

with open('first_file.txt', 'w') as f1, open('second_file.txt', 'w') as f2:

    for line in lines:

        match = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.0\b', line)
        if match:

            f1.write(line)
        else:

            f2.write(line)


with open('first_file.txt', 'r') as f1, open('second_file.txt', 'r') as f2:
    count1 = len(f1.readlines())
    count2 = len(f2.readlines())
    print(f'Количество строк в первом файле: {count1}')
    print(f'Количество строк во втором файле: {count2}')
