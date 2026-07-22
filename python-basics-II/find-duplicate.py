some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []

for i,_ in enumerate(some_list):
    j = i + 1
    while(j < len(some_list)):
        if(some_list[i] == some_list[j]):
            duplicate.append(some_list[i])
            break
        j +=1

# for item in some_list:
#     if(some_list.count(item) > 1):
#             if item not in duplicate:
#              duplicate.append(item)


print(duplicate)
