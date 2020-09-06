# реализация без отлова ошибок

from sys import argv
employee = argv[1]
work_hours = int(argv[2])
usd_per_hour = int(argv[3])
bonus = int(argv[4])
total_salary = work_hours * usd_per_hour + bonus
print(f'Employee {employee} will have salary {total_salary}')