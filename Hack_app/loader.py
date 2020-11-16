import os

clear = lambda: os.system('cls')
clear()

programs = input("What program do you wish to run? \n1.Flood\n2.Keylogger\n3.Subdomain-finder\n4.Exit\n ")
programs = str(programs)
i = 0

while i == 0:
    if programs == "1":
        clear()
        exec(open("Hack_app\\Flood\\flood_app.py").read())
        break
    elif programs == "2":
        clear()
        exec(open("Hack_app\\Keylogger\\keylogger_app.py").read())
        break
    elif programs == "3":
        clear()
        exec(open("Hack_app\\Subdomain_finder\\subdomain_app.py").read())
        break
    elif programs == "4": 
        clear()
        print("Exiting..")
        exit()
    else:
        clear()
        print("This is not a valid input, please try again")
        programs = input("What program do you wish to run? \n1.Flood\n2.Keylogger\n3.Subdomain-finder\n ")