import socket
import os
from requests import get

clear = lambda: os.system('cls')
console_color = lambda: os.system('color a')
console_color()
clear()

start_program = input("---> What's your IP <---\n\nDo you wish to start the program? [y/n]\n")

q1 = 0
q2 = 0

while q1 == 0:
    if start_program == "y":
        clear()
        break
    elif start_program == "n":
        clear()
        q2 += 1
        return_to_loader = input("Do you wish to return to the main loader? [y/n]\n")
        break
    else:
        clear()
        print("This is not a valid input, please try again\n")
        start_program = input("---> What's your IP <---\n\nDo you wish to start the program? [y/n]\n")

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
        return_to_loader = input("Do you wish to return to the main loader? [y/n]\n")

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
public_ip = get("https://api.ipify.org").text

print(f"Hostname: {hostname}")
print(f"Local IP: {local_ip}")
print(f"Public IP: {public_ip}")