"""
Домашнее задание 19
Написать в отдельном модуле функцию count_day подсчета количества дней между двумя датами с использованием методов модуля datetime. Функция принимает два параметра в формате даты, например, count_day(12.01.2021, 15.02.2021) и выдает целое число
"""

import datetime


class NewModul:

    def date_diff(self, date_1: str, date_2: str) -> int:
        date_1 = list(map(int, date_1.split('.')))
        date_2 = list(map(int, date_2.split('.')))
        diff = datetime.date(date_1[2], date_1[1], date_1[0]) - \
            datetime.date(date_2[2], date_2[1], date_2[0])
        return abs(diff.days)


Days = NewModul()
amount = Days.date_diff(input('Введите 1-ю дату: '),
                        input('Введите 2-ю дату: '))

print(f"\nРазница между датами в днях - {amount}")
