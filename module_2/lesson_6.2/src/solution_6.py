goods: list[str] = input('Введите товары через запятую: ').split(', ')

new_index: int = int(input('Позиция для нового товара: ')) - 1

new_product: str = input('Введите новый товар: ')

goods.insert(new_index, new_product)

print(f"Товары на полке: {', '.join(goods)}")