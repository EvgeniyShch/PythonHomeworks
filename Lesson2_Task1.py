list1 = []
for el in range(30):
    list1.append(el/2)
    list1.append(f'word{el**3}')
    list1.append(None)
    list1.append({el: f'name{el}'})
    list1.append([el, el+1, el+2])
    list1.append((el, el-1, el-2))
    list1.append(bin(el))
    
for el in list1:
    print(f'{el} is {list1.index(el)} element of List and has {type(el)}')
    