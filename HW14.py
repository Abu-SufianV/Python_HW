"""
Домашнее задание 14

Создайте собственный модуль, поместив в него ваши функции, созданные в предыдущих заданиях. Напишите любую программу с использованием функций этого модуля.
"""
import math


class MainModule:

    def __init__(self) -> None:
        print("Объект MainModule создан успешно!")

    def calculation(self, x, y, operation: str, ):
        x = int(x)
        y = int(y)
        self.result = 0
        if operation == '+':
            return x + y
        elif operation == '-':
            return x - y
        elif operation == '*':
            return x * y
        elif operation == '/':
            return x / y

        print('Неизвестная операция')
        return None

    def gcf(self, x: int, y: int) -> int:
        x = int(x)
        y = int(y)

        while (x > 0 and y > 0):
            if x > y:
                x, y = x % y, y
            else:
                x, y = x, y % x
        return max(x, y)

    def equation(self, *args: int):
        if len(args) == 3:
            a, b, c = args
            disc = b ** 2 - 4 * a - c
            if disc < 0:
                return []
            x1 = (-1 * b + math.sqrt(disc)) / (2 * a)
            x2 = (-1 * b - math.sqrt(disc)) / (2 * a)
            if x1 == x2:
                return [round(x1, 2)]
            else:
                return [round(x1, 2), round(x2, 2)]
        elif len(args) == 2:
            b, c = args
            x = (-1 * c) / b
            return [round(x, 2)]
        elif len(args) == 1:
            if args[0] == 0:
                return ["*"]
            else:
                return []
        else:
            return None


obj = MainModule()
print(f"Calculation: {str(obj.calculation(21, 227, '/'))}")
print(f"GCF: {str(obj.gcf(15, 100))}")
print(f"Equation: {str(obj.equation(13, 12, 4))}")
