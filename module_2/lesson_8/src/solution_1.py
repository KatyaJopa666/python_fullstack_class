goods: dict[str, int] = {'Яблоко':100, 'Банан':80, 'Кофе':250, 'Чай':150}

product: str = input('Введите товар: ')

try:
    print(f"Цена: {goods[product]}")

except KeyError:
    print(f'Такого товара нет в словаре!')
