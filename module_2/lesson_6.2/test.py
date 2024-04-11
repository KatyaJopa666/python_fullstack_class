# Primes: list[int] = [2, 3, 5, 7, 11, 13]
# Rainbow: list[str] = ['Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубой', 'Синий', 'Фиолетовый']

def content_enumerator(a):
    counter: int = 0
    for i in a:
        print(f'{counter} element is {i}')
        counter += 1
    print()

# content_enumerator(Primes)
# content_enumerator(Rainbow)

# str_primes: list[str] = list(map(str, Primes))

# print(str_primes)

print('List creating.')

# manual list input
# list_size: int = int(input('Enter lisr size number: '))
# new_list: list[str] = [input(f'Enter element value: ') for i in range(list_size)]

'''
# хз как использовать counter
list_input_counter: int = 0
new_list: list[str] = [input(f'Enter {list_input_counter} element value: ') for i in range(list_size)]
'''
# static list
new_list: list[str] = ['a', 'b', 'c', 'd', 'e'] # р

content_enumerator(new_list)

print(new_list[4:-1:-1])

list_2: list[int] = [1, 2, 3, 4, 5]
print('2nd element is ', list_2[2])
list_2[2:4] = [7, 8, 9]
print(list_2)