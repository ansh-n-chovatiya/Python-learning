# def highest_even(arr):
#     """
#     Test doc string
#     """
#     highest_even = arr[0]

#     for item in arr:
#         if item % 2 == 0 and item > highest_even:
#             highest_even = item

#     return highest_even


# print(highest_even([10, 2, 3, 4, 8, 11]))

# a = "hellloooooooooo"

# if (n := len(a)) > 10:
#     print(f"Too long {n} elements")


# while n := len(a) > 1:
#     print(n)
#     print("A", a[:-1])
#     a = a[:-1]


# sum_var = 0


# def test_fun():
#     global sum_var

#     sum_var = sum_var + 1


# print(sum_var)

# test_fun()

# print(sum_var)


x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    print(x)


outer()
