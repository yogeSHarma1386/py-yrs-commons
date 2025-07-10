from functools import wraps

from yrs_commons.utils.log import y_print


def yrs_ignore_memorise(func):  # pragma: no cover
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


def yrs_rprint(*f_args, pad_length = None, **f_kwargs):  # pragma: no cover
    """
    Sample usage:
    @yrs_rprint()
    def subarraySum(self, nums: list[int], k: int) -> int:
        pass

    @yrs_rprint(pad_length=15)
    def subarraySum(self, nums: list[int], k: int) -> int:
        pass

    :param f_args:
    :param pad_length:
    :param f_kwargs:
    :return:
    """
    def o_wrap(func):
        @wraps(func)
        def i_wrap(*args, **kwargs):
            ret_value = func(*args, **kwargs)
            to_print = f"{ret_value} <= {func.__name__} | Parameters<(args: {args[1:]} kwargs: {kwargs})>"

            y_print(pad_length or len(str(ret_value)), to_print, **f_kwargs)
            return ret_value
        return i_wrap
    return o_wrap
