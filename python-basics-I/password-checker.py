username = input("Please Enter Your Username:\n")
password = input("Please Enter Your Password:\n")

password_length = len(password)
secret = "*" * password_length

print(f"Hi {username}, Your password {secret} is {password_length} characters long")
