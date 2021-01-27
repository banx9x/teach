def do_twice(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner
