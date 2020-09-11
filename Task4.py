dict_number = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',\
               'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}
with open("task4_input.txt", "r") as new_file_task4_1:
    word_number = []
    for i in new_file_task4_1:
        stroka = i.split(" ", 1)
        word_number.append(" ".join((dict_number.get(stroka[0]), stroka[1])))
with open("task4_output.txt", "w") as new_file_task4_2:
    new_file_task4_2.writelines(word_number)