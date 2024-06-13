#Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
#метод, который выводит информацию о товаре в формате "Название: название,
#Цена: цена, Количество: кол-во".

class tovar:

    def __init__(self, nazvanie, price, kolvo):
        self.nazvanie = nazvanie
        self.price = price
        self.kolvo = kolvo
    def infovivod(self):
        print(f"Название: {self.nazvanie}, Цена: {self.price}, Количество: {self.kolvo}")


tovar = tovar("Айфон", 100000, 5)

tovar.infovivod()