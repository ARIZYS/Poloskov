#1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Содержимое первого файла:
#Четные элементы:
#Количество четных элементов:
#Среднее арифметическое:
#Содержимое второго файла:
#Нечетные элементы:
#Количество нечетных элементов:
#Сумма положительных элементов:
import random


nums1 = [random.randint(-100, 100) for i in range(10)]
nums2 = [random.randint(-100, 100) for i in range(10)]
with open("even_numbers.txt", "w") as f1:
    for num in nums1:
        f1.write(str(num) + "\n")
with open("odd_numbers.txt", "w") as f2:
    for num in nums2:
        f2.write(str(num) + "\n")


with open('even_numbers.txt', 'r') as f1:
    even_numbers = [int(x) for x in f1.read().split()]

with open('odd_numbers.txt', 'r') as f2:
    odd_numbers = [int(x) for x in f2.read().split()]

even_count = len([x for x in even_numbers if x % 2 == 0])
even_mean = sum(even_numbers) / even_count


odd_count = len([x for x in odd_numbers if x % 2 != 0])
odd_sum_positive = sum([x for x in odd_numbers if x > 0])


with open('result.txt', 'w') as f:
    f.write(f"Содержимое первого файла:\n")
    f.write(f"Четные элементы: {even_numbers}\n")
    f.write(f"Количество четных элементов: {even_count}\n")
    f.write(f"Среднее арифметическое: {even_mean:.2f}\n")
    f.write(f"\nСодержимое второго файла:\n")
    f.write(f"Нечетные элементы: {odd_numbers}\n")
    f.write(f"Количество нечетных элементов: {odd_count}\n")
    f.write(f"Сумма положительных элементов: {odd_sum_positive}")