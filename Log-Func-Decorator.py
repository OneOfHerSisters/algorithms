from typing import Callable
from functools import wraps

def log_func(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"func {func.__name__} args {args} kwargs {kwargs}")
    return wrapper
