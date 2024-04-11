goods: list[str] = input('Введите товары через запятую: ').split(', ')

index_to_delete: int = int(input('Позиция для удаления товара: ')) - 1

goods.pop(index_to_delete)

print(f"Товары на полке: {', '.join(goods)}")

