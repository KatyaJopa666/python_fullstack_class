# решение, соответствующее описанию задания:

prices: list[int] = [int(i) for i in input('Введите цены: ').split(', ')]

odd_prices: list[str] = []

for i in prices:
    if i%2 != 0:
        odd_prices.append(str(i))
        i += 1

print(f"Цены без скидки: {', '.join(odd_prices)}")


# # решение, соответствующее таблице входных и выходных данных:

# prices: list[str] = input('Введите цены: ').split(', ')

# print(f"{', '.join(prices[1::2])}")

