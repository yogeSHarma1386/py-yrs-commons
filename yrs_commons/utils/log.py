
__DEFAULT_PAD_STR = ' '

__TYPE_SPECIFIC_PAD = {
    (int, True): __DEFAULT_PAD_STR,   # Treat empty fields as space-padded
    (int, False): '0',                # Non-empty, use zero padding

    (str, True): __DEFAULT_PAD_STR,   # Normal space padding
    (str, False): '-',                # Fill with dash if string is short

    (float, True): __DEFAULT_PAD_STR, # Float gets space padding
    (float, False): '0',              # Float gets zero padding
}


def y_print(pad_length: int, *args,
    is_empty_fill: bool = True, float_precision: int = 2, **kwargs):


    def format_value(value):
        pad_char = __TYPE_SPECIFIC_PAD.get((type(value), is_empty_fill), None)

        if pad_char is None: return value
        elif isinstance(value, float):
            formatted = f"{value:.{float_precision}f}"
        else:
            formatted = str(value)

        return formatted.rjust(pad_length, pad_char)

    formatted_args = [format_value(arg) for arg in args]
    print(*formatted_args, **kwargs)

