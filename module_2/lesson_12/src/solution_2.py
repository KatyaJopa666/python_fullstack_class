from typing import Callable

def check_order(items: list[str]) -> bool:
    return bool(items)


def package_order(order_id: int) -> str:
    return f'Упакован заказ {order_id}'


def send_order(
               checking_func: Callable[[list[str]], bool],
               packing_func: Callable[[int], str],
               order: dict[str: int, str: list[str]]
               ) -> str:
    
    if checking_func(order['items']):
        return f"Отправка: {packing_func(order['id'])}"
    else:
        return f"Отправка: Заказ {order['id']} пуст"


order1 = {'id': 1, 'items': ['book', 'pen']}
order2 = {'id': 2, 'items': []}

print(send_order(check_order, package_order, order1))
print(send_order(check_order, package_order, order2))


