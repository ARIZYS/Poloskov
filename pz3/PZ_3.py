#Дано трехзначное число. Проверить истинность высказывания:
#«Цифры данного числа образуют возрастающую последовательность»
a = int(input("Введите трёхзначное число :  "))
while (a < 100) or (a > 999):
    a = int(input("Ошибка! Введите трёхзначное число!:  "))

a1 = (a // 100)
print(a1)
a2 = (a % 100)//10
print(a2)
a3 = (a % 10)
print(a3)

if ((a2-a1==1) and (a3-a2==1)):
    print(a, "Цифры данного числа образуют возрастную последовательность")
else:
    print(a,"Цифры данного числа не образуют возрастную последовательность")