#Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N).
#Найти среднее арифметическое всех элементов списка, кроме элементов с номерами от K до L включительно.
def calc(lst, K, L):
    if not (1 < K <= L <= len(lst)):
        print("Ошибка: Некорректные значения K и L.")
        return None

    elm = lst[:K-1] + lst[L:]

    if elm:
        average = sum(elm) / len(elm)
        return average
    else:
        print("В исключенном диапазоне нет элементов.")
        return None

N = 10
i = 0
list = []
while i < N:
    b = int(input("Введите значение в список"))
    i += 1
    list.append(b)
K = int(input("Введите значение, большее одного"))
L = int(input("Введите второе значение, большее одного"))

result = calc(list, K, L)
print(f"Среднее арифметическое всех элементов, кроме от {K} до {L}: {result}")