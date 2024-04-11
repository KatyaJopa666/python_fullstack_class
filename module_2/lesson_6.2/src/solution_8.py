goods: list[str] = input('Введите товары: ').split(', ')

swap_indexes: list[int] = [int(i) - 1 for i in input('Позиции для перестановки: ').split(', ')]

goods[swap_indexes[0]], goods[swap_indexes[1]] = goods[swap_indexes[1]], goods[swap_indexes[0]]

print(f"На полке: {', '.join(goods)}")
                           