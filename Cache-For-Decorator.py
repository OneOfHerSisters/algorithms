from typing import Callable
import time


def cache_for(*, seconds: int):
    def wrapper(func: Callable):
        cache = {}

        def inner(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key not in cache or time.time() - cache[key][1] > seconds:
                res = func(*args, **kwargs)
                cache[key] = [res, time.time()]
                print("run")
                return res
            else:
                print("cache")
                return cache[key][0]

        return inner
    return wrapper
