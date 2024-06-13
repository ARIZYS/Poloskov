#Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
#элементов.

import random

matrix = [[random.randint(1, 10) for i in range(4)] for i in range(4)]

print("Исходная матрица:")
for row in matrix:
    print(row)


for i, row in enumerate(matrix):
    if i % 2 != 0:
        average = sum(row) / len(row)
        print("Среднее арифметическое элементов в строке", i ,":",average)
