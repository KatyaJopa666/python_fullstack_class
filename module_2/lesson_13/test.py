# from typing import Callable

# def my_decorator(function_to_decorate: Callable[[], None]) -> Callable[[], None]:
#     def wrapper():
#         print("Before function call")
#         function_to_decorate()
#         print("After function call")
#     return wrapper


# def decorator_1(function_to_decorate: Callable[[], None]) -> None:
#     print("Before function call")
#     function_to_decorate()
#     print("After function call")
    

# @decorator_1
# # @my_decorator
# def old_function():
#     print("You ain't changing me!")

# print(type(decorator_1))
# print(type())
# print(type(old_function))

# old_function()

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Функция обёртка"""
        print("Что-то происходит до вызова функции.")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def show():
    """Просто функция"""
    print("Функция была вызвана.")

show()
print(show.__name__)
print(show.__doc__)