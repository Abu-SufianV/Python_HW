def index_sort_abs(arr: list) -> list[int]:
    return list(map(lambda x: arr.index(x), sorted(arr)))


num = [5.2, 0.3, 0.0, 15.4, -2.1]
print(index_sort_abs(num))
