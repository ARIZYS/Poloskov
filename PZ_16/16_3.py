#Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
#метод, который выводит информацию о товаре в формате "Название: название,
#Цена: цена, Количество: кол-во".



#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате

import pickle

class product:
    def __init__(self, nazvanie, price, kolvo):
        self.nazvanie = nazvanie
        self.price = price
        self.kolvo = kolvo

    def display_info(self):
        print(f"Название: {self.nazvanie}, Цена: {self.price}, Количество: {self.kolvo}")

def save_def(obj_list, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj_list, f)

def load_def(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


product1 = product("Айфон", 100000, 5)
product2 = product("Самсунг", 80000, 10)
product3 = product("Нокия", 50000, 15)

save_def([product1, product2, product3], "tovars.pickle")


tovars_list = load_def("tovars.pickle")


for tovar in tovars_list:
    tovar.display_info()
