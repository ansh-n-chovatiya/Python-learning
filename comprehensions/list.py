my_list = [item ** 2 for item in range(0, 100) if item % 2 == 0]

# for item in "Hello":
#     my_list.append(item)

print(my_list)


some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'a', 'n', 'n']


duplicate = list(set([i for i in some_list if some_list.count(i) > 1]))

print(duplicate)