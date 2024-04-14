# tuple_1 = (['a', 'b'])
# print(tuple_1)

list_1 = [1, 2, 3, 4]
set_1 = {1, 2}

b = set_1.intersection(list_1)
print(b)

# d = list_1.intersection(set_1)
# print(d)

set_1.add('a')
print(set_1)

dict_1: dict[str:str | float] = {'1':2.0, 'Имя':'Виктор'}
print(dict_1)

a = dict_1['1']
print(a)

print(f"{'1' in dict_1}")

print(list(dict_1.values()))

dict_1[(1, 2, 3)] = 'Один, Два, Три'
print(dict_1)

b = 1
dict_1[b] = 'Бэ'

print(dict_1)

dict_2: dict = dict(Igor = 'Игорь')
print(dict_2)

c=b
d = [1, 2]
a = {b, c}
print(a)

a = {1, 2, 3}
b = {1}
print(a - b)