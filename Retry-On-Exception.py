def retry_on_exception(retries: int):
    def wrapper(func):
        def inner(*args, **kwargs):
            count = 0
            while count < retries:
                try:
                    res = func(*args, **kwargs)
                    print("ok")
                    return res
                except Exception as e:
                    count += 1
                    if count < retries:
                        print(f"{type(e).__name__}")
                    else:
                        print(f"final {type(e).__name__}")
        return inner
    return wrapper
