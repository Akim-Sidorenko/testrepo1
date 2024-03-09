#Вариант 6
#Написать класс Shape, который является родительскимдля
# класса Square, который содержит конструктор, принимающий длину.
# Оба класса содержат метод area() для расчета площади.
# Причем класс Shape имеет площадь равную нулю
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

# Пример использования:
# Получаем длину стороны от пользователя
length = float(input("Введите длину стороны квадрата: "))
# Создаем объект Square с введенной длиной стороны
square = Square(length)

# Выводим площадь квадрата
print("Площадь квадрата:", square.area())

# Создаем объект Shape (родительский класс)
shape = Shape()

# Выводим площадь фигуры (в данном случае будет 0)
print("Площадь фигуры:", shape.area())