def gcf(x, y):
    while x > 0 and y > 0:
        if x > y:
            x, y = x % y, y
        else:
            x, y = x, y % x
    return max(x, y)


print(gcf(int(input()), int(input())))
