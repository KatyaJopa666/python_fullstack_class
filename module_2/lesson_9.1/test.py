# def sum(a: int, b: int) -> int:
#     c: int = a + b
#     return c
# print (sum(1, 2))

# def divide(a: float, b: float) -> float:
#     c: int = a / b
#     print(f'a = {a}, b = {b}, a / b = {c}')
# divide(2, 3)

# divide(b = 4, a = 6)

def print_test():
    e: int = d + 1
    print(f'check {e}')
d: float = 0
print_test()
print(d)

def f():
    global a
    a = 3
    a += 1
    print(a)
a = 0
f()
print(a)