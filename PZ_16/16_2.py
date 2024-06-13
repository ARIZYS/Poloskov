#Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
#класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
#переопределите методы, связанные с вычислением площади и периметра.
class figura:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def ploshad(self):
        return self.width * self.height

    def perimetr(self):
        return 2 * (self.width + self.height)

class rectangle(figura):
    pass

class square(figura):
    def __init__(self, side):
        super().__init__(side, side)

    def ploshad(self):
        return self.width ** 2

    def perimetr(self):
        return 4 * self.width


ширина_прямоугольника = int(input("Введите ширину прямоугольника: "))
высота_прямоугольника = int(input("Введите высоту прямоугольника: "))
сторона_квадрата = int(input("Введите сторону квадрата: "))


rectangle = rectangle(ширина_прямоугольника, высота_прямоугольника)
square = square(сторона_квадрата)


print(f"Площадь прямоугольника: {rectangle.ploshad()}")
print(f"Периметр прямоугольника: {rectangle.perimetr()}")
print(f"Площадь квадрата: {square.ploshad()}")
print(f"Периметр квадрата: {square.perimetr()}")
