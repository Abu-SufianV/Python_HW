"""
Домашнее задание 11

Создайте текстовый файл, содержащий информацию о товарах и ценах на них. Каждая строка файла имеет вид: НАЗВАНИЕ ТОВАРА: ЦЕНА. Используя данный файл добавьте в файл информацию о трех новых товарах таким образом, что:

- Если в файле еще нет строки с таким названием, то новый товар добавляется

- Если в файле уже есть строка с таким названием, то новая строка не добавляется, а в уже существующей строке изменяется цена
"""


GOODS = {'Футболка': 700,
         'Шорты': 1200,
         'Кепка': 600,
         'Рубашка': 1700,
         'Пиджак': 7000,
         'Пальто': 12000}

with open('goods.txt', 'w', encoding='UTF-8') as FILE:
    for key, value in GOODS.items():
        FILE.write(f'{key}: {value}\n')


def add_goods_in_file(file_path: str, name: str, price: int) -> None:
    with open(file_path, 'r', encoding='UTF-8') as file:
        lines = {}
        for row in file:
            word = row.replace('\n', '').split(': ')
            lines[word[0]] = word[1]

    lines[name] = price
    with open(file_path, 'w', encoding='UTF-8') as file:
        for k, v in lines.items():
            file.write(f'{k}: {v}\n')


amount = int(input('Какое кол-во товаров Вы хотите добавить: '))

for i in range(0, amount):
    print()
    good_name = input('Название: ')
    good_price = int(input('Цена: '))
    add_goods_in_file('goods.txt', good_name, good_price)
