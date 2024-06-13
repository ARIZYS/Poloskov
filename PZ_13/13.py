#В матрице найти минимальный элемент в предпоследнем столбце.
import random

matrix = [[random.randint(1, 9) for i in range(5)] for i in range(5)]


print("Исходная матрица:")
for row in matrix:
    print(row)


column = [row[3] for row in matrix]
min = min(column)

print("Минимальный элемент в предпоследнем столбце:",min)