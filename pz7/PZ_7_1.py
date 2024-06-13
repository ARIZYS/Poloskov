#1. Дана строка, изображающая целое положительное число. Вывести сумму цифр этого числа.
def sum_of_digits(number_str):
    if not number_str.isdigit():
        print("Ошибка: Введите строку, представляющую целое положительное число.")
        return None

    total_sum = sum(int(digit) for digit in number_str)
    return total_sum

input_str = input("Введите строку, представляющую целое положительное число: ")

result = sum_of_digits(input_str)

print("Сумма цифр числа:", result)