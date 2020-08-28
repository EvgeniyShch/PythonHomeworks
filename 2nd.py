userseconds = int(input("Введите количество секунд"))

hours = userseconds//3600
minutes = userseconds%3600//60
seconds = userseconds%3600%60

usertime ="{}{}:{}{}:{}{}".format(hours//10,hours%10,minutes//10,minutes%10,seconds//10,seconds%10)

print(f"Введенное Вами количество {userseconds} секунд в формате ЧЧ:MM:CC равняется {usertime} ")


import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)