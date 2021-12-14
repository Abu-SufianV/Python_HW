"""
Задача 3.

Есть список целых чисел, например a = [6, 7, 1, 4, 9, 3, 0, 10, 12, 18], длина которого не превосходит 10.
Напишите функцию, которая находит для списка монотонно неубывающую подпоследовательность максимальной длины.
Вернуть надо число - длину максимальной подпоследовательности и один из возможных вариантов подпоследовательности.
Список из одного элемента считается монотонной последовательностью (подпоследовательностью) длины 1.
Если входящий список пустой, то вернуть надо ноль и пустой список.
"""

import copy


def mono_subsequence(arr):
    subsequences = []
    subsequence = []

    for i in range(1, len(arr)):
        if arr[i - 1] <= arr[i]:
            subsequence.append(arr[i - 1])
        else:
            subsequence.append(arr[i - 1])
            subsequences.append(copy.copy(subsequence))
            subsequence = []

    if subsequence:
        subsequences.append(copy.copy(subsequence))

    max_subsequence = []
    for subsequence in subsequences:
        if len(subsequence) > len(max_subsequence):
            max_subsequence = subsequence
    return len(max_subsequence), max_subsequence


print(mono_subsequence([6, 7, 1, 4, 9, 3, 0, 10, 12, 18]))

