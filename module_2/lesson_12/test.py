# from typing import Callable

# def factory_of_multipliers(by=2) -> Callable[[int], int]:
#     def multiply(val: int) -> int:
#         return val * by
#     return multiply

# # print(factory_of_multipliers)
# print(factory_of_multipliers(4)(10))

# def empty():
#     return print(1)
    
# # print(type(empty()))
# # print(type(print('yeah')))

# empty()

# dict_1 = {'no': 1}

# print(dict_1['no'])

# dict_2 = {'1': 1, 'items': [1]}
# print(bool(dict_2['items']))
# print(type(f'Упакован заказ '))

print(type(lambda value: value % 2 != 0))