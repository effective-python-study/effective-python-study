# functools.wrap을 사용해 데코레이터를 정의하라
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
            f'-> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """주어진 수에 해당하는 피보나치 수를 반환한다."""
    if n in (0, 1):
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))

fibonacci(4)

print(fibonacci)
help(fibonacci)

from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
            f'-> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return n 번째 피보나치 수"""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))

help(fibonacci)