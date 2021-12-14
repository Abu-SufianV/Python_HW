"""
Задача 3
Напишите функцию, которая по строке, являющейся параметром функции, составляет словарь,
ключами которого являются все встречающиеся в строке символы, а значениями - количество этих символов в строке.
"""


def uniq_letter(line: str) -> dict[str: int]:
    dict_letter = {}

    for s in line:
        if s in dict_letter:
            dict_letter[s] += 1
        else:
            dict_letter[s] = 1

    return dict_letter


for k, v in uniq_letter('Hello, world!!!').items():
    print(f"'{k}' - {v}")
