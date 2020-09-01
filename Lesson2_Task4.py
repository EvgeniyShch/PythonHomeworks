string1 = input("Введите строку")
list1 = string1.split(" ")

for inc, el in enumerate(list1):
    print(inc, el[0:10])