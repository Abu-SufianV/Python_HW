def area_triangle(x1: tuple, x2: tuple, x3: tuple) -> float:
    return abs(0.5 * ((x2[0] - x1[0]) * (x3[1] - x1[1]) - (x3[0] - x1[0]) * (
            x2[1] - x1[1])))


print(area_triangle((2, -3), (1, 1), (-6, 5)))
