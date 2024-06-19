from typing import Callable

def type_checker(func: Callable) -> None:
    def checker(*args) -> None:
        if len(args) != 2:
            print(f'Ошибка! Количество аргументов не равно двум!')
        elif type(args[0]) != str:
            print(f'Ошибка! Первый аргумент не строка!')
        elif type(args[1]) != int:
            print(f'Ошибка! Второй аргумент не число!')
        else:
            func(*args)
    return checker


@type_checker
def estimate_time(*args) -> None:
    print('Estimated time calculated successfully')


estimate_time('Веб-сайт', 'пять')
estimate_time('Визитка', 10)