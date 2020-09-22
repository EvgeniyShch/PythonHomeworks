class Orgteknika:
    price = 0
    paper_use: bool
    numb = 0
    my_store, my_store_full = [], []
    def __init__(self, name, quantity, *args, **kwargs):
        self.name = name
        self.quantity = quantity
        self.my_unit = {'Модель ': self.name, 'Цена ': self.price, 'Количество': self.quantity}
        self.numb += 1

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def insertion(self):
        while True:
            try:
                unit = input(f'Введите наименование для класса {self.__class__.__name__} ')
                unit_q = int(input(f'Введите количество '))
                self.my_unit = {'Модель ': unit, 'Цена ': self.price, 'Количество': unit_q}
                self.my_store.append(self.my_unit)
                print(f'Текущий список товаров -\n {self.my_store}')
            except:
                print('Ошибка ввода данных')
            else:
                choice = input(f'Для выхода нажмите - Q, для продолжения - Enter\n')
                if choice.upper() == 'Q':
                    self.my_store.insert(0, self.__class__.__name__)
                    self.my_store_full.append(list(i for i in self.my_store))
                    self.my_store.clear()
                    print(f'Выход из программы из класса {self.__class__.__name__}')
                    return f'Весь склад -\n {self.my_store_full}'
                else:
                    continue

class Printer(Orgteknika):
    price = 100
    paper_use = True
    def to_print(self):
        return f'to print smth {self.quantity} times'

class Scaner(Orgteknika):
    price = 200
    paper_use = False
    def to_scan(self):
        return f'to scan smth {self.quantity} times'
class Xerox(Orgteknika):
    price = 150
    paper_use = True
    def to_copy(self):
        return f'to copy smth  {self.quantity} times'

unit_1 = Printer('HP', 2000, 5, 10)
unit_2 = Scaner('Sony', 1200, 5, 10)
unit_3 = Xerox('Samsung', 1500, 1, 15)
print(unit_1, unit_2, unit_3, sep="\n")
print(unit_1.insertion())
print(unit_2.insertion())
print(unit_3.insertion())
print(unit_1.to_print())
print(unit_3.to_copy())