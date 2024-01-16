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
    {red}|1| {green}Ddos 1           {red}|2| {green}Ddos 2                                                     
    {green}―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)
def execute_command(command):
    if command == '1':
        os.system('python ddos.py')
    elif command == '2':
        os.system('python dos.py')


while True:
    display_menu()
    command = input('>>>>>>')

    if command.lower() == 'exit':
        break

    execute_command(command)