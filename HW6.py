import os


def open_file(name: str):
    path = os.path.abspath('Алгоритмы и структуры данных Python/'+name)
    if os.path.isfile(path):
        with open(path) as f:
            return f.read()
    else:
        return '404. File {0} not found'.format(name)


print(open_file(input('Введите название файла: ')))
