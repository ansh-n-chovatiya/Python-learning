arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(item):
    return item % 2 == 0


new_arr = list(filter(is_even, arr))

print(new_arr)
