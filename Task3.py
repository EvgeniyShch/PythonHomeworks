class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                self.my_list.append(int(input('Введите значение для записи в массив\n')))
                print(f'Текущий список массива - {self.my_list}')
            except:
                check = input(f'Пользователь может вводить только числа.\nПопробовать еще раз? Y/N ')
                if check.upper() == 'Y':
                    continue
                else:
                    return f'Запись завершена. Итоговый массив {self.my_list}'

try_except = Error()
print(try_except.my_input())