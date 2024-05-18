def discounts(cost: int, visits: int) -> int:
    discounted: int = cost
    if visits >= 20:
        discounted = 0.8 * cost
    elif visits >= 10:
        discounted = 0.9 * cost
    print(f'Цена: {cost}, Посещений: {visits}    Итоговая цена: {discounted}')

discounts(100, 5)
discounts(200, 10)
discounts(150, 20)