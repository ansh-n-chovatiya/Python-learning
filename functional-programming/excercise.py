from functools import reduce


# def f_score(item):
#     return item > 50


# def c_total(acc, item):
#     return acc + item


# 3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# filtered_scores = filter(lambda item: item > 50, scores)
# total = reduce(lambda acc, item: acc + item, filtered_scores, 0)

# print("total", total)


# list_power = [3, 8, 9, 2]

# print(list(map(lambda i: i * i, list_power)))

tupple_array = [(0, 2), (4, 3), (9, 9), (10, -1)]

sorted_array = tupple_array.copy()
sorted_array.sort(key=lambda item: item[1])

# for i in range(0, len(sorted_array)):

#     for j in range(i, len(sorted_array)):
#         if (sorted_array[j][1] < sorted_array[i][1]):
#             temp = sorted_array[j]
#             sorted_array[j] = sorted_array[i]
#             sorted_array[i] = temp


print(sorted_array)
