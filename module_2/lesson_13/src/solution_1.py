from typing import Callable

def logger(func: Callable[[str, int, int], None]) -> Callable[[str, int, int], None]:
    def notification(item: str, new_price: int, price: int) -> None:
        func(item, new_price, price)
        print(f'Цена на {item} изменилась! {new_price} > {price}')
    return notification


@logger
def change_price(item: str, new_price: int, price: int) -> None:
    return None


change_price('Кресло', 5000, 4500)
change_price('Стол', 8000, 7600)
