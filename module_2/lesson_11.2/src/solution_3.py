def track_low_stock_with_for(goods: dict[str: int], req_quant: int) -> None:
    print('Низкий запас:')
    low_quant_counter: int = 0
    for item in goods:
        if goods[item] < req_quant:
            print(f'{item} — {goods[item]}')
            low_quant_counter += 1
    if low_quant_counter == 0:
        print('все запасы в норме.')
    

track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)