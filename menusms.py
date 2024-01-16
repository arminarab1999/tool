import sys,os
from colorama import Fore
import time
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
def display_menu():
    print(f"""
    {green}―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    {red}|1| {green}sms/python           {red}|2| {green}sms/golang                                                     
    {green}―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)
def execute_command(command):
    if command == '1':
        os.system('python bmb.py')
    elif command == '2':
        os.system('go run sms.go')
    elif command == '3':
        os.system('')
    elif command == '4':
        os.system('')
    elif command == '5':
        os.system('')
    elif command == '6':
        os.system('')
    elif command == '7':
        os.system('')


while True:
    display_menu()
    command = input('>>>>>>')

    if command.lower() == 'exit':
        break

    execute_command(command)