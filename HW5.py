"""
Домашнее задание 5

Напишите функцию, которая находит максимум функции f(x) в точках отрезка [a,b] с постоянным шагом h. Параметрами функции являются f, a, b, h. Параметры a, b, h – необязательные, по умолчанию a=0, b=1, h=0.1. Используя эту функцию, найдите максимум функции (6-x)sin(x/6) на отрезке [0, 12].
"""

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
