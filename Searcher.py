from requests import get
from rich import *
from concurrent.futures import ThreadPoolExecutor
import os


if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print("""
                                                             [blue]1.1[/blue]                                      [blue]For programmers[/blue] 
                                                           [magenta]
                              ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ ▓█████  ██▀███  
                            ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
                            ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░▒███   ▓██ ░▄█ ▒
                              ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
                            ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
                            ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
                            ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
[blue]>Admin Founder[/blue]              ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░   ░     ░░   ░ 
[blue]>Make By: DOCKTYPE[/blue]                  ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░   ░  ░   ░     
                                                              ░ [/magenta]                                
                                                          [blue]we are everywer![/blue]
""")

# لیستی برای ذخیره لینک‌های موفق
successful_links = []

def check_url(url):
    full_address = site + "/" + url
    response = get(full_address)
    if response.status_code == 200:
        print(f"[green]{full_address} OK [/green]")
        successful_links.append(full_address)
    else:
        print(f" [red]{full_address} Not found [/red]")
site = input("Enter a Target Site Url: ")
site = site.replace("http://", "").replace("https://", "").replace("www.", "")
site = "http://" + site
Urls = ("urls.txt")
Urls = open(Urls, "r").read().splitlines()
num_threads1 = input("Speed and power(Between 1 and 20 or more): ")
num_threads = int(num_threads1)

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(check_url, Urls)


print("\n[green]Successful Links:[/green]")
for link in successful_links:
    print(f"[green]{link}[/green]")
