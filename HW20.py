"""
Домашнее задание 20

Средствами numpy рассчитать произведения четных чисел от 2 до 20 на числа, которые больше их на единицу
"""


import numpy as np

numbers = []
for i in range(2, 21):
    if i % 2 == 0:
        numbers.append(i+1)

print(numbers)
print(np.prod(numbers, dtype=np.double))
