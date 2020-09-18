class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if quantity < 1:
            self._quantity = 2
        else:
            self._quantity = quantity

    def func_decorator(func):
        def func_wrapper(*args, **kwargs):
            print(func.__name__, end="")
            result = func(*args, **kwargs)
            return result
        return func_wrapper

    def __str__(self):
        return f'Результат = клетка из {self.quantity} звезд : {self.quantity * "*"}'

    @func_decorator
    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    @func_decorator
    def __sub__(self, other):
        return Cell(self.quantity - other.quantity) if (self.quantity - other.quantity) > 0 \
            else f'Разность количества ячеек двух клеток < 0'

    @func_decorator
    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    @func_decorator
    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, limit):
        return f'{"*" * limit}\n' * (self.quantity // limit) + f'{"*" * (self.quantity % limit)}'

cell1 = Cell(11)
cell2 = Cell(0)
print(cell1)
print(cell2)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print((cell1 * cell2) * (cell1 - cell2) - (cell1 - cell2) * (cell1 / cell2))
print(cell1.make_order(3))
print(cell1.make_order(5))
print(cell1.make_order(15))