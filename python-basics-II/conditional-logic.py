is_old = False
is_license = False

if is_old and is_license:  
    print("The user is able to drive the car")
else: 
   if is_old == False and is_license == False:
      print("User does not have licesnse and not old enough to drive a car")
   elif is_license == False:
      print("User does not have license, not eligible to drive car")
   else:
     print("User is not old enough to drive a car, not eligible to drive car")

is_old = 0
is_boolean_flag = ""

if(is_old):
   print("All number expact 0 are truthy values even negative once")

if(is_boolean_flag):
   print("test log")


print("User is old enough") if is_old else print("User is not old enough")