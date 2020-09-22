class Data:

    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        return " ".join([i for i in day_month_year.split() if i != "-"])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Дата введена верно'
                else:
                    return f'Год введен неверно'
            else:
                return f'Месяц введен неверно'
        else:
            return f'День введен неверно'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


print(Data.extract('21 - 09 - 2020'))

today = Data('21 - 09 - 2020')
print(today)
print(today.extract('22 - 09 - 2020'))

print(Data.valid(21, 9, 5555))
print(today.valid(21, 21, 2020))
print(Data.valid(121, 9, 2020))
print(Data.valid(21, 9, 2020))