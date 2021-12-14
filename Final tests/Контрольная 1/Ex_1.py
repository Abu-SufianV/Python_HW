"""
Задача 1
Напишите функцию, параметрами которой являются список из целых чисел и целое число.
Функция должна вернуть среднее значение элементов списка, которые больше параметра - целого числа.
"""


def average_value(array: list[int], val: int) -> float | str:
    need_nums = []

    for i in array:
        if i > val:
            need_nums.append(i)

    if len(need_nums) == 0:
        return f'В данной списке нет числе, которые больше {val}'
    return sum(need_nums) / len(need_nums)


print(average_value([1, 2, 3, 4, 5, 6], 3))
