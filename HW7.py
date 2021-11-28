"""
Домашнее задание 7

Напишите функцию умножения неограниченного количества чисел. Если аргумент не является числом, то должна вызываться ошибка ValueError
"""


def multiply_func(*args: int):
    total = 1
    for i in args:
        if isinstance(i, str):
            return 'ValueError'
        total *= i
    return total


print("Ответ: {}".format(multiply_func(5, 7, 8, 2)))
