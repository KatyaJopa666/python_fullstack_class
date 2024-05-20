def count_specific_items_with_while(goods: list[str], req_item: str) -> None:
    req_items_count: int = 0
    while len(goods) > 0:
        if goods[0] == req_item:
            req_items_count += 1
        goods.pop(0)
    print(f"Количество '{req_item}': {req_items_count}")

count_specific_items_with_while(['fruit', 'toy', 'fruit', 'toy'], 'toy')
count_specific_items_with_while(['clothes', 'clothes', 'clothes'], 'clothes')