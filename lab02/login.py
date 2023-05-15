import json
from project import *

    
def login():
    email = input("Enter email address: ")
    password = input("Enter password: ")
    with open("users.json", "r") as f:
            data = json.load(f)
    for user in data:
        # print(user)
        # print(user['email'])
        if user['email'] == email and user['password'] == password:
            print("Successfuly login")
            print(user['user_id'])
            project_menue(user['user_id'])
        else:
            print("Invalid email or password.")
    



