goods: dict[str, int] = {'Яблоко':100, 'Банан':80, 'Кофе':250, 'Чай':150}

cheap_product: str = min(goods, key=goods.get)
expensive_product: str = max(goods, key=goods.get)

print(f'Самый дешевый: {cheap_product} — {goods[cheap_product]} руб.')
print(f'Самый дорогой: {expensive_product} — {goods[expensive_product]} руб.')