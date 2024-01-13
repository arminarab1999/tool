import sys,os 
import socket 
from datetime import datetime
#color
pink='\033[35m'
red='\033[31m'
green='\033[32m'
blue='\033[36m'
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
#next
print(f"""{blue}
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
█       █       █   ▄  █ █       █  █       █       █      █  █  █ █  █  █ █       █   ▄  █  
█    ▄  █   ▄   █  █ █ █ █▄     ▄█  █  ▄▄▄▄▄█       █  ▄   █   █▄█ █   █▄█ █    ▄▄▄█  █ █ █  
█   █▄█ █  █ █  █   █▄▄█▄  █   █    █ █▄▄▄▄▄█     ▄▄█ █▄█  █       █       █   █▄▄▄█   █▄▄█▄ 
█    ▄▄▄█  █▄█  █    ▄▄  █ █   █    █▄▄▄▄▄  █    █  █      █  ▄    █  ▄    █    ▄▄▄█    ▄▄  █
█   █   █       █   █  █ █ █   █     ▄▄▄▄▄█ █    █▄▄█  ▄   █ █ █   █ █ █   █   █▄▄▄█   █  █ █
█▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄█  █▄█ █▄▄▄█    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄█  █▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█
      """)
print(f"{red}>>> Enter your host ip address , Example '192.168.10.10' <<<")
host = socket.gethostbyname(input(f"{pink}Enter your host ip address: "))
print(f"{blue}―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print(f"{red}>>> Enter the range, Example '50' <<<")
ports = input(str(f"{green}Enter range between 1 to 1000: "))
print(f"{blue}―――――――――――――――――――――――――――――――――――――――――――――――――――――――")
print("-" * 50)
print("scanning  target" + host)
print("Time started" + str(datetime.now()))
print("-" * 50)
try:
             for port in range(int(ports)):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = s.connect_ex((host,port))
                    if result == 0:
                            print(F"Following {port} is open")
                    s.close()
         
except KeyboardInterrupt:
    print("\r Exiting program")

except socket.gaierror:
    print("Host name could not be solved")
    sys.exit()
except socket.error:
    print("could not connect")
    sys.exit()