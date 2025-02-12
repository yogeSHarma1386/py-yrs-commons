# ============= Recursion Implementation =============
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Negative numbers not allowed")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def power(base: int, exponent: int) -> int:
    if exponent < 0:
        raise ValueError("Negative exponent not allowed")
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    half = power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    return half * half * base
