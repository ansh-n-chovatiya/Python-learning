a = [1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0}
print(res)


arr = {item: item ** 2 for item in range(0, 10) if item % 2 != 0}
print("🚀 ~ arr:", arr)
