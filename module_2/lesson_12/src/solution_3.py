from typing import Callable

def filter_data(
               values: list[int],
               condition: Callable[[int], bool]
               ) -> str:
    
    result: list[int] = [i for i in values if condition(i)]
    print (f'Отфильтрованные данные: {result}')
    

data_sets = [
            ([10, 23, 35, 47], lambda x: x % 2 != 0),
            ([5, 7, 8, 10], lambda x: x > 7),
            ([1, 2, 3, 5, 6], lambda x: x < 5),
            ([10, 20, 30, 40, 50], lambda x: x % 5 == 0 and x % 8 == 0)
            ]

for data, filter_func in data_sets:
    filtered_data = filter_data(data, filter_func)
    