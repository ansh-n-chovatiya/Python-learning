# for item in "Test string":
#   print(item)

# name_arr = ["Ansh", "Nayan", "Chovatiya", "Test"]

# test_num_array = list(range(1,6))

# for item in test_num_array:
#    for char in ['a','b','c']:
#       print(item, char)


# user = {
#     "name": "Ansh Chovatiya",
#     "can_swim": True,
#     "age": 22, 
#     "gender": "Male"
# }


# for item in user:
#     print(f"{item} - {user[item]}")


# for item in user.items():
#     print(f"{item}")


# for key, value in user.items():
#     print(f"{key} - {value}")


# print(enumerate("Hello"))

# for item in enumerate("Hello"):
#     print(item)


# for key, value in enumerate(list(range(31,100))):
#     if(value == 50):
#         print(f"The index of number 50 is {key}")


counter = 0


# while(counter < 10):
#      print(f"The counter value is {counter}")
#      counter += 1


while(counter < 10):
     counter += 1
     
     if(counter == 25 ):
          break
     
     if(counter == 5):
          continue
     
     print(f"The counter value is {counter}")
else:
     print("Loop operation has ended")