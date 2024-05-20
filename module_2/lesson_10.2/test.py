def factorial(n):
    if n == 0:
        print(f'функция остановлена, n = {n}')
        return 1
    print(f'n = {n}, n * (n -1) = {n * (n-1)}')
    return n * factorial(n - 1)

print(factorial(10))

# def wtf(x):
#     if x == 3:
#         return('x = 3')
#     return x * wtf(x - 1)

# print(wtf(10))

# def what_the_fuck(a):
#     if a == True:
#         return 'функция остановлена'
#     print('или нет?')
#     return what_the_fuck(a-1)

# print(what_the_fuck(2))