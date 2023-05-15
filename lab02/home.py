# import
from login import *
from register import *
from project import *

while True:
    print("\n1- Register\n2- Login")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register()
    elif choice == 2:
        login()

    else:
        print("Invalid choice, Please try again")
    
