"""
Домашнее задание 3

Дана дробь 𝑛/𝑚 , n и m - натуральные числа. Напишите 2 функции, которые сокращают эту дробь, то есть находят числа p и q такие, что 𝑛/𝑚 = 𝑝/𝑞 , и дробь 𝑝/𝑞 — несократимая:

• аргументами функции являются числа n, m, функция возвращает кортеж (p, q);

• аргументом функции является список [n, m], функция не возвращает значения, а изменяет этот список на [p, q].

Для поиска НОД воспользуйтесь функцией из Домашнего задания 2.
"""


def gcf(x, y):
    while x > 0 and y > 0:
        if x > y:
            x, y = x % y, y
        else:
            x, y = x, y % x
    return max(x, y)


def reduce_fraction_num(x, y) -> tuple:
    fraction = gcf(x, y)
    result = (int(x / fraction), int(y / fraction))
    return result


def reduce_fraction_arr(array: list) -> list:
    fraction = gcf(array[0], array[1])
    result = [int(array[0] / fraction), int(array[1] / fraction)]
    return result


print(reduce_fraction_num(10, 15))
print(reduce_fraction_arr([10, 15]))
