def repeater(repeat: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeat):
                val = func(*args, **kwargs)
            return val
        return wrapper
    return decorator


@repeater(3)
def greeting(name):
    print(f"I've been expecting you, {name}!")


# greeting("Nikolay")