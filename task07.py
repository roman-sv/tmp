# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

#https://ru.onlinemschool.com/math/assistance/complex_number/calculation/


class ComplexNumbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):

        return f'Сумма: {self.x + obj.x}+{self.y + obj.y}i'

    def __mul__(self, obj):

        return f'Произведение: {self.x * obj.x - self.y * obj.y}+{self.y * obj.x + self.x * obj.y}i'


a = ComplexNumbers(4, -6)
b = ComplexNumbers(5, 5)

print(a + b)
print(a * b)
