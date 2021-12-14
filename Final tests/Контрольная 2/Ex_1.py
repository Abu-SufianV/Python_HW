"""
Задача 1.

Напишите функцию, параметром которой является имя текстового файла. Надо прочитать текст, разбить его на строчки и проверить,
образуют ли первые символы каждой строчки полиндром. Полиндром - это такая строка, которая не изменяется,
если все ее символы записать в обратном порядке. Например - "abba". Результат функции - логическое значение - True или False.
В качестве результата выполнения задания кроме функции и примера ее вызова надо также загрузить в кампус пример файла.

"""


def palindrome_file(path: str):
    with open(path, 'r') as FILE:
        rows = list(filter(None, FILE.read().split('\n')))
        line = ''
        for row in rows:
            line += row[0]

    return line == ''.join(reversed(line))


print(palindrome_file('text.txt'))
