from datetime import datetime

birth_year = input("What year is your birth year\n")

user_age = datetime.now().year - int(birth_year)

print(f"Your birth year is {birth_year} and your age is {user_age}")
