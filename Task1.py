with open("task1.txt", "w") as new_file_task1:
    i = 1
    while True:
        inputted_line = input(
            f"Введите данные для {i} строки в файл {new_file_task1.name}. Для окончания записи данных нажмите Enter.\n")
        if inputted_line == "":
            break
        i += 1
        new_file_task1.write("{0}\n".format(inputted_line))

# Недостаток решения создается последняя строка после последнего ввода Enter, просьба подсказать как этого избежать