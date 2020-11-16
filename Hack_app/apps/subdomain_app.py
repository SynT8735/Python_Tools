import requests
import os

clear = lambda: os.system('cls')
clear()

start_program = input("Created by SynT8735\nThis is a Subdomain Finder\nIt should only be used in safe/legal enviromnents\nDo you wish to start the program?\n[y/n]\n")

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
        start_program = input("Created by SynT8735\nThis is a Subdomain Finder\nIt should only be used in safe/legal enviromnents\nDo you wish to start the program?\n[y/n]\n")

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


domain = input('eg: hackthissite.org\nEnter domain: ')

file = open('req\\subdomains.txt', 'r')

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("Discovered Subdomain: ", url)