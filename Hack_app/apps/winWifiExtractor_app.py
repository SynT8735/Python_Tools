import subprocess
import os

clear = lambda: os.system('cls')
console_color = lambda: os.system('color a')
console_color()
clear()

start_program = input("---> Windows Wifi Extractor <---\n\nDo you wish to start the program? [y/n]\n")

q1 = 0
q2 = 0
q3 = 0

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
        start_program = input("---> Windows Wifi Extractor <---\n\nDo you wish to start the program? [y/n]\n")

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

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Cannot be read!')

return_or_leave = input("\nDo you wish to return to the main loader? [y/n]\n")
q3 = 1

while q3 == 1:
    if return_or_leave == "y":
        clear()
        exec(open("loader.py").read())
        break
    elif return_or_leave == "n":
        clear()
        print("Exiting..")
        exit()
