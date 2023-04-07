# 7 - Ask the user for his name then confirm that he has entered his name
# (not an empty string/integers). then proceed to ask him for his email and
# print all this data
# - (Bonus) check if it is a valid email or not
import re

# Email Validation fun
def is_valid_email(email):
    pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})\b'
    return re.match(pattern,email)

def confirm_user():
    while True:
        name = input("Please Enter your Name: ")
        if name:
            break
        print("Not Valid Name, Please Try Again")
    while True:
        email = input("Enter your email: ")
        if is_valid_email(email):
            break
        print("Invalid Email, Please Try Again")

    print("Name: ", name)
    print("Email: ", email)

confirm_user()