import sys

a: int = 0
print('\na =', a, '\nsys.getsizeof(a) =', sys.getsizeof(a))

a: str = 'a'
print('\na =', a, '\nsys.getsizeof(a) =', sys.getsizeof(a))

a: str = ''
print('\na =', a, '\nsys.getsizeof(a) =', sys.getsizeof(a))

a: str = 'а'
print('\na =', a, '\nsys.getsizeof(a) =', sys.getsizeof(a))
