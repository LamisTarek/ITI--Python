import re
import json
import uuid

def validate_first_name():
    str=input("Enter your firstName: ")
    if str !="" and str.isalpha():
       return str
    else:
        if str == "":
            print("firstName is required")
        else:
            print("firstName must be characters only")
        return validate_first_name()

def validate_last_name():
    str=input("Enter your lastName: ")
    if str !="" and str.isalpha():
       return str
    else:
        if str == "":
            print("lastName is required")
        else:
            print("lastName must be characters only")
        return validate_last_name()

def validate_mail():
    email= input("Enter your email: ")
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
      return email
    else:
      print("Invalid email")
      return validate_mail()
    
def validate_password():
    password= input("Enter your password: ")
    if  password.isdigit() == False and password !="":
        print("Invalid password")
        return validate_password()
    else:
        confirmed =confirm_pass(password)
        if confirmed:
            return password
        else:
            return validate_password()

def confirm_pass(password):
    confirmed= input("Enter your confirmed password: ")
    if  confirmed == password:
        return True
    else:
        print("Invalid, please try again")
        return confirm_pass(password)
    
def validate_phone(phone):
    pattern = r"^(01)[0125][0-9]{8}$"
    return bool(re.match(pattern, phone))

def save_data(user):
    with open('users.json', 'r') as file:
        users = json.load(file)
    users.append(user)
    with open('users.json', 'w') as file:
        json.dump(users,file)



def register():
    first_name = validate_first_name()
    last_name = validate_last_name()
    email = validate_mail()
    password = validate_password()
    mobile_phone= input("Enter your mobile phone: ")
    if not validate_phone(mobile_phone):
        print("Unmatcehd Egyption number, Please try again")
        return
    user_id= uuid.uuid4()
    print(user_id)
    
    user={
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'mobile_phone': mobile_phone,
        'user_id':str(user_id)
    }
    save_data(user)
   