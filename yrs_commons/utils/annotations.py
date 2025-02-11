def yrs_ignore_memorise(func):  # pragma: no cover
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper
