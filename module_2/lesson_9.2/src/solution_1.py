prices_n_discount: list[int] = [int(i) for i in list(input('Введите цены и скидку: ').split(', '))]

def discount_sum(list_1: list[int]) -> int:
    return int(sum(list_1[:-1]) * list_1[-1] / 100)

print(f'Сумма скидки: {discount_sum(prices_n_discount)}')
