import math


def function(x: float) -> float:
    return (6 - x) * math.sin(x / 6)


def max_func(func, a: int = 0, b: int = 1, h: float = 0.1) -> float:
    m = func(a)
    while a <= b:
        m = max(func(a), m)
        a += h
    return m


print(max_func(function, 0, 12))
