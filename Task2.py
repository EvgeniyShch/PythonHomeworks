with open("task2.txt", "r") as new_file_task2:
    for numberline, line  in enumerate(new_file_task2, 1):
        stroka = line.split()
        print(f"В {numberline} cтроке {len(stroka)} слов(а)")
    print(f'Всего файле {numberline} строк')