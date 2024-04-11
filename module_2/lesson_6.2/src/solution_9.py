prices: list[int] = [int(i) for i in input('Введите цены: ').split(', ')]

prices.sort()

print(f"Отсортированные цены: {prices[::-1]}")