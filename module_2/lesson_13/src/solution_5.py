from typing import Callable

def token_checker(authorization: Callable[[str, str], None]) -> Callable[[str, str], None]:
    def checker(name: str, password: str) -> None:
        if name == 'Роман' and password == 'correctpassword':
            authorization(name, password)
        else:
            print('В доступе отказано!')
    return checker


@token_checker
def access_client_data(name: str, password: str) -> None:
    print('Доступ получен. Данные: ...')

access_client_data('Роман', 'correctpassword')
access_client_data('Олег', 'wrongpassword')