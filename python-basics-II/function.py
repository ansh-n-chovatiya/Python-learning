# def test_function(name='placeholder', age=32):
#     print(f"Hello {name}, your age is {age}")

# def sum(ar1, ar2):
#     return ar1 + ar2

# test_function('ansh',22)
# test_function(age=22, name="ansh")
# test_function()
# test_function(None, age=42)

# print(sum(3, 8))


def super_func(*arg, **named):
    return {"direct": sum(arg), "Named": sum(named.values())}


print(super_func(1, 2, 3, 3, 5, n1=8, n2=5, n3=2))
