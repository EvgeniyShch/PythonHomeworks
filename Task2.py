def func_user_data():
    while True:
        try:
            name = input("Введите свое имя\n")
            surname = input("Введите свою фамилию\n")
            year_of_birth = int(input("Укажите год рождения\n"))
            city = input("Укажите город проживания\n")
            email = input("Укажите свой email\n")
            telephone_number = int(input("Укажите свой номер телефона\n"))
            full_user_info = name + " " + surname + ", " \
            + str(year_of_birth) + " года рождения, из города " + city \
     	    + ". почта : " + email + " ; телефон : " + str(telephone_number)
            break
        except ValueError as error1:
            print("Данные введены неверно", error1)
    return full_user_info
    
print(f'Пользовательские данные :\n{func_user_data()}')