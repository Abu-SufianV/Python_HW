"""
Задача 2.

Заданы две заранее неизвестные строки в которых слова разделены пробелами.
Из двух строк надо составить одну, в котрой слова из первой и второй строки будут чередоваться, при этом порядок слов
будет сохранен. (Если длины списков не равны, то "остаток" более длинного списка целиком дописывается в строку)
Пример: 'один два три', 'альфа бетта гамма' -> 'один альфа два бетта три гамма'
"""


def rows_join(line_1: str, line_2: str) -> str:
    line_1 = line_1.split()
    line_2 = line_2.split()

    result_line = []
    if len(line_1) > len(line_2):
        str_len = len(line_2)
        equal = 1
    elif len(line_1) < len(line_2):
        str_len = len(line_1)
        equal = 2
    else:
        str_len = len(line_1)
        equal = 0

    for i in range(str_len):
        result_line.append(line_1[i])
        result_line.append(line_2[i])

    if equal == 1:
        for i in range(len(line_2) - 1, len(line_1)):
            result_line.append(line_1[i])
    elif equal == 2:
        for i in range(len(line_1) - 1, len(line_2)):
            result_line.append(line_2[i])

    return ' '.join(result_line)


print(rows_join(input('Введите 1-ю строку: '), input('Введите 2-ю строку: ')))
