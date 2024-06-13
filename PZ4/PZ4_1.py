#Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
#X - X3/3 + X5/5 - ... + (-1)NX2N +1/(2N +1). Полученное число является приближенным
#значением функции arctg в точке X
import math

def arctan(X, N):
    result = 0
    sign = 1

    for i in range(1, 2 * N + 2, 2):
        term = sign * (X ** i) / i
        result += term
        sign *= -1

    return result


X = input("Введите число большее нуля, но меньше, чем один:  ")
N = input("Введите число, большее нуля:   ")
while type(X) != float:
    try:
        X = float(X)
    except ValueError:
        print("Не соблюдается условие!")
        X = input("Введите число X")
while type(N) != int:
    try:
        N = int(N)

    except ValueError:
        print("Условие не соблюдается")
        N = input("Введите число N")

if X >= 1:
    print("Введите меньшее значение X ")
elif X <= 0:
    print("Введите большее значение X")
elif N <= 0:
    print("Введите большее значение N")
else:
    result = arctan(X, N)
    exact_value = math.atan(X)

    print(f"Приближенное значение arctan({X}) для N = {N}: {result}")
    print(f"Точное значение arctan({X}): {exact_value}")