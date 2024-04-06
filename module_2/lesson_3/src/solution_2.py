# employee_1: str = 'Света'
# employee_2: str = 'Олег'
# employee_3: str = 'Маша'
# employee_4: str = 'Паша'

# print('В чётные дни работают:', employee_1, employee_2)
# print()
# print('В нечётные дни работают:', employee_3, employee_4)




employees: list = ['Света', 'Олег', 'Маша', 'Паша']
# employees: list = input('Введите имена сотрудников через пробел: ').split(' ')

even_days_employees: list = []
odd_days_employees: list = []

i=0
for employee in employees:
    if i < len(employees) / 2:
        even_days_employees.append(employees[i])
        i +=1
    else:
        odd_days_employees.append(employees[i])
        i +=1

print('В чётные дни работают:', ' '.join(even_days_employees))
print()
print('В нечётные дни работают:', ' '.join(odd_days_employees))