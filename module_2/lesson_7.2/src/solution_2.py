numbers: list[int] = [int(i) for i in input('Введите список: ').split(', ')]

print(f'Сумма подсписка: {sum(numbers[1:4])}')