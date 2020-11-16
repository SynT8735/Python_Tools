import requests
import os
import random
import string
import json

clear = lambda: os.system('cls')
clear()

start_program = input("Created by SynT8735\n\nThis is a database account flooder\nIt should only be used in safe/legal enviromnents\nDo you wish to start the program?\n[y/n]\n")

q1 = 0
q2 = 0

while q1 == 0:
    if start_program == "y":
        clear()
        break
    elif start_program == "n":
        clear()
        q2 += 1
        return_to_loader = input("Do you wish to return to the main loader?\n[y/n]\n")
        break
    else:
        clear()
        print("This is not a valid input, please try again")
        start_program = input("Created by SynT8735\n\nThis is a database account flooder\nIt should only be used in safe/legal enviromnents\nDo you wish to start the program?\n[y/n]\n")

while q2 == 1:
    if return_to_loader == "y":
        clear()
        exec(open("loader.py").read())
        break
    elif return_to_loader == "n":
        clear()
        print("Exiting..")
        exit()
    else:
        clear()
        print("This is not a valid input, please try again")
        return_to_loader = input("Do you wish to return to the main loader?\n[y/n]\n")

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

request_url = input("eg: https://stearmcornnumitti.com/auth/login\nEnter RequestURL: ")  # Input is based from website to website
username_field = input("eg: username\nEnter username: ") # Input is based from website to website
password_field = input("eg: password\nEnter password: ") # Input is based from website to website
password_range = input("How long should be the passwords (>8): ")

while password_range != 8 or password_range < 8:
    password_range = input("Passwords should be atleast 8 characters long: ")
else:
    pass

names = json.loads(open('req\\names.json').read())
emails = json.loads(open('req\\emails.json').read())

print("Starting account flood: ")

for name in names:
    name_extra = ''.join(random.choice(string.digits))
    random_email_choice = random.choice(emails)

    username = name.lower() + name_extra + random_email_choice
    password = ''.join(random.choice(chars) for i in range(password_range))

    requests.post(request_url, allow_redirects=False, data={
        username_field : username, 
        password_field : password  
    })
    
    print('sending username %s and password %s' % (username, password))