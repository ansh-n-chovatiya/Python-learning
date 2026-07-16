print("Sum", 2 + 4)
print("Minus", 5 - 2)
print("Multiply", 4 * 8)
print("Divide", 8 / 4)


print(type(4))
print(type(-4))
print(type(4.9))

print(4 + 1.1, type(4 + 1.1))
print(4.9 + 5.1, type(4.9 + 5.1))

print(5**3)
print(2 // 4)
print(225 // 4)
print(225 / 4)
print(219 // 4)
print(219 / 4)


testVar = 3
testVar2 = 4

x, y, z = 4, 3, 8

print(testVar + testVar2)
print(x, y, z)


print(type("Heloo there"))


lString = """
Hello,

this is multiline big string

bottom
"""

print(lString)

first_name = "ansh"
last_name = "chovatiya"

full_name = first_name + " " + last_name

print(full_name)


print(first_name[0])
print(first_name[0:3])
print(first_name[len(first_name) - 1])


temp_var = "01234567"

print(temp_var[1:6:2])  # 135
print(temp_var[1:])  # 1234567
print(temp_var[:5])  # 01234
print(temp_var[::2])  # 0246
print(temp_var[-8])
print(temp_var[-4])


print(temp_var[::-2])


temp_str = "hello this is all about me"
temp_capital = "HELLO IN CAPITAL"

print(temp_str.upper())
print(temp_capital.lower())

print(temp_capital.replace("IN", "123"))
