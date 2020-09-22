class Complex_Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):

        print('Сумма z1 и z2 - ', end="")
        return Complex_Number(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print('Произведение z1 и z2 - ', end="")
        return Complex_Number(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __str__(self):
        return f'Комплексное число = целая часть {self.a} и мнимая часть {self.b}*i'


z_1 = Complex_Number(1, -2)
z_2 = Complex_Number(3, 4)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)