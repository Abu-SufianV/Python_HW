from typing import List


def mid_element(array: List[float]):
    setlist = set(array)
    if (len(array) % 2 == 0) or (len(array) == 0) or (
            len(array) != len(setlist)):
        return ValueError("incorrect values list")
    array.sort()
    num = (len(array) - 1) // 2
    return array[num]


print(mid_element([2.13, 3.14, 5.00, 0.55, 0]))
