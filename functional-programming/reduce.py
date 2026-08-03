from functools import reduce


arr = [10, 20, 30]


def sum(ar1, ar2):
    return ar1 + ar2


new_array = reduce(sum, arr, 5)

print(new_array)
