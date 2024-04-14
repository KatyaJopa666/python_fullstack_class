goods: dict[str, int] = {'Яблоко':100, 'Банан':80, 'Кофе':250, 'Чай':150}

prices: list[int] = list(goods.values())

max_price_index: int = prices.index(max(prices))
min_price_index: int = prices.index(min(prices))

product_names: list[str] = list(goods.keys())

max_price_product: str = product_names[max_price_index]
min_price_product: str = product_names[min_price_index]

print(f'Самый дешевый: {min_price_product} — {min(prices)} руб.')
print(f'Самый дорогой: {max_price_product} — {max(prices)} руб.')