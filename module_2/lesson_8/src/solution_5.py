first_shop: set[str] = set(input('Первый магазин: ').split(', '))
second_shop: set[str] = set(input('Второй магазин: ').split(', '))

print(f"Только в первом магазине: {', '.join(first_shop - second_shop)}")
print(f"Только во втором магазине: {', '.join(second_shop - first_shop)}")