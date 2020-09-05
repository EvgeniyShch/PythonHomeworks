
def func_user_data(name, surname, year_of_birth, city, email, telephone_number):
    full_user_info = name + " " + surname + ", " \
    + str(year_of_birth) + " года рождения, из города " + city \
    + ". почта : " + email + " ; телефон : " + str(telephone_number)
    return full_user_info

while True:
        try:
            name1 = input("Введите свое имя\n")
            surname1 = input("Введите свою фамилию\n")
            year_of_birth1 = int(input("Укажите год рождения\n"))
            city1 = input("Укажите город проживания\n")
            email1 = input("Укажите свой email\n")
            telephone_number1 = int(input("Укажите свой номер телефона\n"))
            
            break
        except ValueError as error1:
            print("Данные введены неверно", error1)
    
print(f'Пользовательские данные :\n{func_user_data(year_of_birth=year_of_birth1, city=city1, name=name1, email=email1, surname=surname1, telephone_number=telephone_number1)}')

# благодаря именованным аргументам функции их можно вводить в любом порядке