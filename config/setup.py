from colorama import Fore, Style
import os
import platform
from isort import file
bn = f'''{Fore.RED}
  █████▒▄▄▄        █████   ▄████▄   ▒█████   ███▄ ▄███▓ ▄▄▄▄    ▒█████  
▓██   ▒▒████▄    ▒██▓  ██▒▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▒██▒  ██▒
▒████ ░▒██  ▀█▄  ▒██▒  ██░▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██░  ██▒
░▓█▒  ░░██▄▄▄▄██ ░██  █▀ ░▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██░█▀  ▒██   ██░
░▒█░    ▓█   ▓██▒░▒███▒█▄ ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░ ████▓▒░
 ▒ ░    ▒▒   ▓▒█░░░ ▒▒░ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▒░▒░ 
 ░       ▒   ▒▒ ░ ░ ▒░  ░   ░  ▒     ░ ▒ ▒░ ░  ░      ░▒░▒   ░   ░ ▒ ▒░ 
 ░ ░     ░   ▒      ░   ░ ░        ░ ░ ░ ▒  ░      ░    ░    ░ ░ ░ ░ ▒  
             ░  ░    ░    ░ ░          ░ ░         ░    ░          ░ ░  
                          ░                                  ░  
                          
            [{Style.RESET_ALL} Telegram{Fore.RED}: @{Style.RESET_ALL}JustFaQ{Fore.RED} ]{Style.RESET_ALL} {Fore.RED}[{Style.RESET_ALL}{platform.python_version()}{Fore.RED}]       
'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()
os.system('pip3 install -r other/requirements.txt')
clear()
print(bn)
print(f"\n{Fore.RED}[{Style.RESET_ALL}+{Fore.RED}] {Style.RESET_ALL}Finished Installing the Libraries, run {Fore.RED}[{Style.RESET_ALL}run_script.cmd{Fore.RED}]{Style.RESET_ALL} or {Fore.RED}[{Style.RESET_ALL}run_script.sh{Fore.RED}]{Style.RESET_ALL}")
