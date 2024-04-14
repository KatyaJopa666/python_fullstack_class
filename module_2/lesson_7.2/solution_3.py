numbers: list[int] = [int(i) for i in input('Введите список: ').split(', ')]

numbers_sublist: list[str] = [str(i) for i in numbers[numbers[0]:numbers[-1]:numbers[1]]]

print(f"Числа подсписка: {', '.join(numbers_sublist)}")