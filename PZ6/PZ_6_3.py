#Дано множество A из N точек (точки заданы своими координатами х, у). Среди всех точек этого множества, лежащих во второй четверти, найти точку,
#наиболее удаленную от начала координат. Если таких точек нет, то вывести точку с нулевыми координатами.
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2 .
#Для хранения данных о каждом наборе точек следует использовать по два списка:
#первый список для хранения абсцисс, второй — для хранения координат.

import math
def point(x_coords, y_coords):
    max_distance = 0
    max_point = (0, 0)

    for x, y in zip(x_coords, y_coords):
        if x < 0 and y > 0:
            distance = math.sqrt(x**2 + y**2)

            if distance > max_distance:
                max_distance = distance
                max_point = (x, y)

    return max_point

x_coordinates = [-1, -2, -3, -4, -5]
y_coordinates = [1, 2, 3, 4, 5]

max_point = point(x_coordinates, y_coordinates)

if max_point != (0, 0):25
    print("Наиболее удаленная точка во второй четверти:", max_point)
else:
    print("В множестве нет точек во второй четверти.")