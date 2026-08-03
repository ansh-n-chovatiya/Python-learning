arr = [3, 8, 29, 39, 23, 10]


def multiply_by_two(item):
    index, value = item
    return value * 2 + index


new_arr = list(map(multiply_by_two, enumerate(arr)))

print("New Array", new_arr)
