def yrs_ignore_memorise(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper
