import math


def equation(*args: int):
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


print(equation(2, 4))
