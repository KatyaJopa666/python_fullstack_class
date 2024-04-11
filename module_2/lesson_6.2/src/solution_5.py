prices: list[int] = [int(i) for i in input('Введите цены: ').split(', ')]

expensivest: int = max(prices)
expensivest_index: int = prices.index(expensivest)

cheapest: int = min(prices)
cheapest_index: int = prices.index(cheapest)

prices[cheapest_index] = expensivest
prices[expensivest_index] = cheapest

print(f"Новые цены: {', '.join(list(map(str, prices)))}")