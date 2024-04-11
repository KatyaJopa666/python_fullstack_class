prices: list[int] = [int(i) for i in input('Введите цены: ').split(', ')]

average: int = round(sum(prices) / len(prices))

print(f'Средняя цена товаров: {average}')