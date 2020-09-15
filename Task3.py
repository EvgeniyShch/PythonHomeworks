class Worker:
    _wage = {"Dvornik": 10000, "Prodavets": 30000, "Programist": 50000}
    _bonus = {"Dvornik": 0, "Prodavets": 1000, "Programist": 3000}
    _income = {"wage": _wage, "bonus": _bonus}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def _get_total_income(self):
        a = Position._income.get("wage").get(self.position)
        b = Position._income.get("bonus").get(self.position)
        try:
            print(f'Зарплата сотрудника {self.surname} = {a}, бонус = {b}, итого {a+b}')
        except Exception as e:
            check = input(f'Должность {self.position} не найдена. Хотите завести новую должность? Y/N\n').upper()
            if check == "Y":
                while True:
                    try:
                        a = Position._income.get("wage").setdefault(self.position, int(input(f"Введите зарплату для должности {self.position}\n")))
                        b = Position._income.get("bonus").setdefault(self.position, int(input(f"Введите бонус для должности {self.position}\n")))
                    except Exception as e:
                        print(e)
                    else:
                        break
                print(f'Должность {self.position} заведена')
                print(f'Зарплата сотрудника {self.surname} = {a}, бонус = {b}, итого {a + b}')
            else:
                print(f'Должность {self.position} не заведена. Зарплата и бонус сотрудника {self.surname} не найдены')


petr = Position("Petr", "Ivanov", "Programist")
petr.get_full_name()
petr._get_total_income()

egor = Position("Egor", "Petrov", "Dvornik")
egor.get_full_name()
egor._get_total_income()

igor = Position("Igor", "Pupkin", "Manager")
igor.get_full_name()
igor._get_total_income()

print()
try:
    alexander = Position()
except Exception as e:
    print(e)
else:
    alexander.get_full_name()
    alexander._get_total_income()