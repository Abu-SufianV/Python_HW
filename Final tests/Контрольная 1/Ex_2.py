"""
Задача 2
Есть список, (например a = [8, 13, 2, 5, 8, 13, 36, 2, 55, 13]).
Напишите функцию, которая оставляет в нем элементы, которые встречаются больше одного раза, а остальные удаляет.
"""


def uniq_nums(array: list[int]) -> list[int]:
    dict_nums = {}
    need_nums = []

    for i in array:
        if i in dict_nums:
            dict_nums[i] += 1
        else:
            dict_nums[i] = 1

    for k, v in dict_nums.items():
        if v > 1:
            need_nums.append(k)

    return need_nums


print(uniq_nums([8, 13, 2, 5, 8, 13, 36, 2, 55, 13]))
