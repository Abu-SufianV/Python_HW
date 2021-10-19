def gcf(x, y):
    while x > 0 and y > 0:
        if x > y:
            x, y = x % y, y
        else:
            x, y = x, y % x
    return max(x, y)


def reduce_fraction_num(x, y) -> tuple:
    fraction = gcf(x, y)
    result = (int(x / fraction), int(y / fraction))
    return result


def reduce_fraction_arr(array: list) -> list:
    fraction = gcf(array[0], array[1])
    result = [int(array[0] / fraction), int(array[1] / fraction)]
    return result


print(reduce_fraction_num(10, 15))
print(reduce_fraction_arr([10, 15]))
