list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [list1[el] for el in range(len(list1)) if list1.count(list1[el]) == 1]
print(result_list)