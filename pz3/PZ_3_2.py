#Даны два числа. Вывести большее из них.
a = int(input("Введите первое число:   "))
b = int(input("Введите второе число:   "))
while (a==b):
    print("Числа равны! Попробуйте снова!")
    a = int(input("Введите первое число:   "))
    b = int(input("Введите второе число:   "))
if a > b:
    print(a)
else:
    print(b)



