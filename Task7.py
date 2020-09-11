import json

with open("task7.txt", "r") as new_file_task7:
    profit, average_profit, dict_profit, final_list, dict_average = 0, [], {}, [], {}
    for line in new_file_task7:
        firm_name, type_property, income, expenses = line.split()
        profit = int(income) - int(expenses)
        if profit > 0:
            average_profit.append(profit)
        dict_profit[f'{firm_name}'] = f'{profit}'
    final_list.append(dict_profit)
    dict_average['average_profit'] = sum(average_profit) / len(average_profit)
    final_list.append(dict_average)
    print(final_list)

with open("task7.json", "w") as new_json_file_task7:
    json.dump(final_list, new_json_file_task7)