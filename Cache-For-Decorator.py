from typing import Callable
import time


def cache_for(*, seconds: int):
    def wrapper(func: Callable):
        cache = {}
        last_time = {}

        def inner(*args, **kwargs):
            if args not in last_time or time.time() - last_time[args] > seconds:
                res = func(*args, **kwargs)
                cache[args] = res
                last_time[args] = time.time()
                print("run")
                return res
            else:
                print("cache")
                return cache[args]

        return inner
    return wrapper
