employees: list = ['Света', 'Олег', 'Маша', 'Паша']
# employees: list = input('Введите имена сотрудников через пробел: ').split(' ')

half: int = int(len(employees) / 2)

print('В чётные дни работают:', ' '.join(employees[:half:]))
print()
print('В нечётные дни работают:', ' '.join(employees[half::]))