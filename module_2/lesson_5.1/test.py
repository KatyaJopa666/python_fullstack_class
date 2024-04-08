# a = '2'
# b = '2'
# c=a+b
# print(c)

a: str = '''
Bla bla
Bla bla
Bla bla'''
print('Test 1' + a)

d = 300
b = 324.235
print('\nTest 2: %10d %.5f' % (d, b))

print('\nTest 3: {0}, {1}, {2}.'.format('first_literal', '2nd', '3rd'))

print('\nTest 4: {d}, {b}'.format(d=d, b=b))

print(f'\nTest 5: {a}')