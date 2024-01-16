import sys,os
from colorama import Fore
import time
import pyttsx3
#next
#color
red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'
# next
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
PlutoPhishing = "DOCKTYPE"
print(f"""{green}
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄█░▄▄▀█▄░▄█░▄▄█░▄▄▀███▄░▄█░████░▄▄███▀▄▄▀█░▄▄▀█░▄▄█░▄▄█░███░█▀▄▄▀█░▄▄▀█░▄▀
██░▄▄▄█░██░██░██░▄▄█░▀▀▄████░██░▄▄░█░▄▄███░▀▀░█░▀▀░█▄▄▀█▄▄▀█▄▀░▀▄█░██░█░▀▀▄█░█░
██░▀▀▀█▄██▄██▄██▄▄▄█▄█▄▄████▄██▄██▄█▄▄▄███░████▄██▄█▄▄▄█▄▄▄██▄█▄███▄▄██▄█▄▄█▄▄█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
code = input("********** :")
if code == PlutoPhishing:
    print("correct password")
else:
    print("Incorrect password")
    sys.exit()
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
#next
time.sleep(1.0)
print(f"{green} ")
print ("                         login - - - !                   ")
print (Fore.YELLOW + "")
print(f"{blue} ")
time.sleep(1.0)
print ("!!")
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
#next
print(f"""{rang}
             =================================================
                        created by DOCKTYPE_GROUP          
             =================================================
―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
 _______    ______     ______  __  ___ .___________.____    ____ .______    _______
|       \  /  __  \   /      ||  |/  / |           |\   \  /   / |   _  \  |   ____|
|  .--.  ||  |  |  | |  ,----'|  '  /  `---|  |----` \   \/   /  |  |_)  | |  |__
|  |  |  ||  |  |  | |  |     |    <       |  |       \_    _/   |   ___/  |   __|
|  '--'  ||  `--'  | |  `----.|  .  \      |  |         |  |     |  |      |  |____
|_______/  \______/   \______||__|\__\     |__|         |__|     | _|      |_______|

                                                                                                                   
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
                                                                 
""")
time.sleep(1.0)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("                                loading . . .                    ")
time.sleep(1.0)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
def display_menu():
    print(f"""{blue}
          

░░░░░░       ░░░░░░       ░░░░░░     ░░   ░░     ░░░░░░░░     ░░    ░░     ░░░░░░      ░░░░░░░ 
▒▒   ▒▒     ▒▒    ▒▒     ▒▒          ▒▒  ▒▒         ▒▒         ▒▒  ▒▒      ▒▒   ▒▒     ▒▒      
▒▒   ▒▒     ▒▒    ▒▒     ▒▒          ▒▒▒▒▒          ▒▒          ▒▒▒▒       ▒▒▒▒▒▒      ▒▒▒▒▒   
▓▓   ▓▓     ▓▓    ▓▓     ▓▓          ▓▓  ▓▓         ▓▓           ▓▓        ▓▓          ▓▓      
██████       ██████       ██████     ██   ██        ██           ██        ██          ███████ 
         
          
           """)
    print(f"""
    {green}―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    {red}|1| {green}Port-Scanner                 {red}|7| {green}none      
    {red}|2| {green}Admin-Finders                {red}|8| {green}none
    {red}|3| {green}Ghost_Tracker                {red}|9| {green}none
    {red}|4| {green}DDOS                         {red}|10| {green}none
    {red}|5| {green}SMS-Bombers                  {red}|11| {green}none
    {red}|6| {green}DoxTracker                   {red}|12| {green}none 
    {green}――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('python port.py')
    elif command == '2':
        os.system('python menuadmin.py')
    elif command == '3':
        os.system('python GhostTR.py')
    elif command == '4':
        os.system('python ddosmenu.py')
    elif command == '5':
        os.system('python menusms.py')
    elif command == '6':
        os.system('python DoxTracker.py')
    elif command == '7':
        os.system('')
    elif command == '8':
        os.system('')
    elif command == '9':
        os.system('')
    elif command == '10':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Keylogger.py"')
    elif command == '11':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Web-Crawler.py"')
    elif command == '12':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Tool/Reverse-Shell.py"')
    else:
        os.system('cls')
        print(Fore.RED + 'Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('>>>>>>')

    if command.lower() == 'exit':
        break

    execute_command(command)