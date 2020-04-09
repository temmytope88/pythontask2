import random
first_name = input("Enter your first name ")
last_name = input("Enter your last name ")
mail = input("enter your email address ")

num = random.randint(10000, 99999)

password = first_name[0:2].upper()+last_name[-2:].upper()+str(num)
passW = input("your password is " + password + ", do you like it? (input yes or no) ")
if passW.upper() == "YES":
    print("your details are:")
    print("First name = " + first_name)
    print("Last name = " + last_name)
    print("Email = " + mail)
    print("Password = " + password)
else:
    password = input("Enter your choice  password ")

    if len(password) < 7:
     password = input("Please a password with or 7 more characters ")
     print("your details are:")
     print("First name = " + first_name)
     print("Last name = " + last_name)
     print("Email = " + mail)
     print("Password = " + password)
    else:
        print("Your details are:")
        print("First name = " + first_name)
        print("Last name = " + last_name)
        print("Email = " + mail)
        print("Password = " + password)

user_details = {}
user_details["FIRST NAME"] = first_name
user_details["LAST NAME"] = last_name
user_details["E-MAIL"] = mail
user_details["PASSWORD"] = password

for key, value in user_details.items():

    print(f'{key}: {value}')












