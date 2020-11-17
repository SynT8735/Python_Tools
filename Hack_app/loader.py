import os

clear = lambda: os.system('cls')
console_color = lambda: os.system('color a')
console_color()
clear()

programs = input("This program was developed by https://github.com/SynT8735/\n\nIt consists in a set of ethical hacking tools meant to be used in a protected/legal environment!\n\nWhat program do you wish to run? \n\n1.Flood\n2.Keylogger\n3.Subdomain-finder\n4.Exit\n ")
programs = str(programs)
i = 0

while i == 0:
    if programs == "1":
        clear()
        exec(open("apps\\flooder_app.py").read())
        break
    elif programs == "2":
        clear()
        exec(open("apps\\keylogger_app.py").read())
        break
    elif programs == "3":
        clear()
        exec(open("apps\\subdomain_app.py").read())
        break
    elif programs == "4": 
        clear()
        print("Exiting..")
        exit()
    else:
        clear()
        print("This is not a valid input, please try again")
        programs = input("What program do you wish to run? \n1.Flood\n2.Keylogger\n3.Subdomain-finder\n ")