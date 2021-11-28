"""
Домашнее задание 9

Дан список, в котором 2n + 1 различных чисел с плавающей точкой. Напишите функцию, которая находит средний элемент списка. Под средним элементом понимают такой, для которого в списке n элементов больше его и n элементов меньше. (Если в списке не 2n + 1 различных элементов, то должна вызываться ошибка)
"""


from typing import List


def mid_element(array: List[float]):
    setlist = set(array)
    if (len(array) % 2 == 0) or (len(array) == 0) or (
            len(array) != len(setlist)):
        return ValueError("incorrect values list")
    array.sort()
    num = (len(array) - 1) // 2
    return array[num]


print(mid_element([2.13, 3.14, 5.00, 0.55, 0]))
