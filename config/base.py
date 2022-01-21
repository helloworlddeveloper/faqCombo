# [+]----------------------------[+]
#  |          fqCombo.py          |
#  |------------------------------|
#  |            Author:           |
#  |          * JustFaq *         |
#  |                              |
#  |           Telegram:          |
#  |         * @JustFaq *         |
#  |------------------------------|
#  |             Date:            |
#  |         * 18/1/2022 *        |
# [+]----------------------------[+]

# [MODULES]------------------------------[+]
from colorama import Fore, Style
import sys
import os
import time
import platform
import getpass
import codecs
import random
import requests
import webbrowser
from isort import file


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 100)

banner = f'''{Fore.RED}
\t\t  █████▒▄▄▄        █████   ▄████▄   ▒█████   ███▄ ▄███▓ ▄▄▄▄    ▒█████  
\t\t▓██   ▒▒████▄    ▒██▓  ██▒▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▒██▒  ██▒
\t\t▒████ ░▒██  ▀█▄  ▒██▒  ██░▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██░  ██▒
\t\t░▓█▒  ░░██▄▄▄▄██ ░██  █▀ ░▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██░█▀  ▒██   ██░
\t\t░▒█░    ▓█   ▓██▒░▒███▒█▄ ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░ ████▓▒░
\t\t ▒ ░    ▒▒   ▓▒█░░░ ▒▒░ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▒░▒░ 
\t\t ░       ▒   ▒▒ ░ ░ ▒░  ░   ░  ▒     ░ ▒ ▒░ ░  ░      ░▒░▒   ░   ░ ▒ ▒░ 
\t\t ░ ░     ░   ▒      ░   ░ ░        ░ ░ ░ ▒  ░      ░    ░    ░ ░ ░ ░ ▒  
\t\t             ░  ░    ░    ░ ░          ░ ░         ░    ░          ░ ░  
\t\t                          ░                                  ░  
\t\t                          
            [{Style.RESET_ALL} Telegram{Fore.RED}: @{Style.RESET_ALL}JustFaQ{Fore.RED} ]{Style.RESET_ALL} {Fore.RED}[{Style.RESET_ALL}{platform.python_version()}{Fore.RED}]     {Fore.RED}[{Style.RESET_ALL}0{Fore.RED}] {Style.RESET_ALL}Telegram Channels       {Fore.RED}[{Style.RESET_ALL}99{Fore.RED}] {Style.RESET_ALL}Exit
'''


def menu():
    clear()
    print(banner)
    print(f"""
        {Fore.RED}[{Style.RESET_ALL}1{Fore.RED}] {Style.RESET_ALL}Filter combo by email domain       {Fore.RED}[{Style.RESET_ALL}2{Fore.RED}] {Style.RESET_ALL}Duplicate remover       {Fore.RED}[{Style.RESET_ALL}3{Fore.RED}] {Style.RESET_ALL}Sort Combo
\n        {Fore.RED}[{Style.RESET_ALL}4{Fore.RED}] {Style.RESET_ALL}Combo line counter                 {Fore.RED}[{Style.RESET_ALL}5{Fore.RED}] {Style.RESET_ALL}Change Split Char       {Fore.RED}[{Style.RESET_ALL}6{Fore.RED}] {Style.RESET_ALL}Email Extractor
\n        {Fore.RED}[{Style.RESET_ALL}7{Fore.RED}] {Style.RESET_ALL}Email To User                      {Fore.RED}[{Style.RESET_ALL}8{Fore.RED}] {Style.RESET_ALL}Combo Extractor         {Fore.RED}[{Style.RESET_ALL}9{Fore.RED}] {Style.RESET_ALL}MAIL:PASS -> PASS:MAIL
\n        {Fore.RED}[{Style.RESET_ALL}10{Fore.RED}] {Style.RESET_ALL}Watermark                         {Fore.RED}[{Style.RESET_ALL}11{Fore.RED}] {Style.RESET_ALL}Combo Shuffler         {Fore.RED}[{Style.RESET_ALL}12{Fore.RED}] {Style.RESET_ALL}Upper the 1st Char of The Password
\n        {Fore.RED}[{Style.RESET_ALL}13{Fore.RED}] {Style.RESET_ALL}Domain Changer                    {Fore.RED}[{Style.RESET_ALL}14{Fore.RED}] {Style.RESET_ALL}Remove a character     {Fore.RED}[{Style.RESET_ALL}15{Fore.RED}] {Style.RESET_ALL}Capture Remove
\n        {Fore.RED}[{Style.RESET_ALL}16{Fore.RED}] {Style.RESET_ALL}Combo Cleaner                     {Fore.RED}[{Style.RESET_ALL}17{Fore.RED}] {Style.RESET_ALL}Combo Scraper/Dumper   {Fore.RED}[{Style.RESET_ALL}18{Fore.RED}] {Style.RESET_ALL}Add Char at the end of pass
\n        {Fore.RED}[{Style.RESET_ALL}19{Fore.RED}] {Style.RESET_ALL}Add Char At The Beginning of The Password  





          """)
    try:
        cmd = int(input(f"\n\t{Fore.RED}┌─$[{Style.RESET_ALL}{getpass.getuser()}{Fore.RED}@{Style.RESET_ALL}JustFaQ{Fore.RED}]-[{Style.RESET_ALL}{os.getcwd()}{Fore.RED}]\n\t└──╼ $ {Style.RESET_ALL}"))
    except ValueError:
        input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}Enter An Integer {Fore.RED}Input{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Try Again{Fore.RED} {Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}")
        menu()
    # Sending The Request Of The User
    req(cmd)


# [REQUESTS]----------------------------[+]
def req(_REQ):
    if _REQ == 0:
         faqTelegram()
    elif _REQ == 99:
        sys.exit()
    elif _REQ == 1:
        faqFilter()
    elif _REQ == 2:
        faqDuplicate()
    elif _REQ == 3:
        faqSort()
    elif _REQ == 4:
        faqCount()
    elif _REQ == 5:
        faqChangeSplit()
    elif _REQ == 6:
        faqEmailExtractor()
    elif _REQ == 7:
        faqEmailToUser()
    elif _REQ == 8:
        faqComboExtractor()
    elif _REQ == 9:
        faqReverse()
    elif _REQ == 10:
        faqWaterMark()
    elif _REQ == 11:
        faqShuffle()
    elif _REQ == 12:
        faqUpperPassword()
    elif _REQ == 13:
        faqDomainChanger()
    elif _REQ == 14:
        faqCharRemove()
    elif _REQ == 15:
        faqCaptureRemove()
    elif _REQ == 16:
        faqComboCleaner()
    elif _REQ == 17:
        faqComboDumper()
    elif _REQ == 18:
        faqCharAtTheEnd()
    elif _REQ == 19:
        faqCharAtTheBeginning()
    else:
        input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}Select an {Fore.RED}Option {Style.RESET_ALL}From The {Fore.RED}Menu{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Try Again{Fore.RED} {Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}")
        menu()    

# [FILTER_DOMAIN]----------------------------[+]

def faqTelegram():
      clear()
      print(banner)
      print(f"""
        {Fore.RED}[{Style.RESET_ALL}1{Fore.RED}] {Style.RESET_ALL}@JustFaQ Channel:  {Fore.RED}[{Style.RESET_ALL}https://t.me/JustFaQTool{Fore.RED}] {Style.RESET_ALL}
\n        {Fore.RED}[{Style.RESET_ALL}2{Fore.RED}] {Style.RESET_ALL}Vandals Cracker TM Channel:  {Fore.RED}[{Style.RESET_ALL}https://t.me/JacktunisHere{Fore.RED}] {Style.RESET_ALL}
\n        {Fore.RED}[{Style.RESET_ALL}3{Fore.RED}] {Style.RESET_ALL}HellCrack Channel:  {Fore.RED}[{Style.RESET_ALL}https://t.me/hellcrack{Fore.RED}] {Style.RESET_ALL}

""")
      try:
         cmd = int(input(f"\n\t{Fore.RED}┌─$[{Style.RESET_ALL}{getpass.getuser()}{Fore.RED}@{Style.RESET_ALL}JustFaQ{Fore.RED}]-[{Style.RESET_ALL}{os.getcwd()}{Fore.RED}]\n\t└──╼ $ {Style.RESET_ALL}"))
         if cmd == 1:
               webbrowser.open('https://t.me/JustFaQTool')
         elif cmd == 2:
               webbrowser.open('https://t.me/JacktunisHere')
         elif cmd == 3:
               webbrowser.open('https://t.me/hellcrack')
      except ValueError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}Select an {Fore.RED}Option {Style.RESET_ALL}From The {Fore.RED}Menu{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Try Again{Fore.RED} {Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}")
         menu()
      menu()
          
def faqCharAtTheBeginning():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqCharBeginningPass'):
           os.mkdir('Output/faqCharBeginningPass')
      if not os.path.isfile('Output/faqCharBeginningPass/faqCharBeginningPass.txt'):
           os.system('echo > Output/faqCharBeginningPass/faqCharBeginningPass.txt')
      try:
         #good = 0
         #bad = 0
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         cmd =input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Char{Style.RESET_ALL} to Add At The Beginning Of The Password:{Style.RESET_ALL} ")
         with open(burn, mode="r", encoding="utf-8") as myFile:
            lines = myFile.readlines()
            with open('Output/faqCharBeginningPass/faqCharBeginningPass.txt', mode="w+", encoding="utf-8") as file1:
               for rows in lines:
                      line = rows.rstrip('\n').split(":")
                      compte = line
                      if len(compte) == 2:
                         pwd = compte[1]
                         pwd = cmd + pwd
                         compte[1] = pwd
                         compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                         file1.write(str(compte) + '\n')
               input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Adding The{Fore.RED} Char{Style.RESET_ALL} At The End Of The Password, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
               menu()
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()

def faqCharAtTheEnd():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqCharEndPass'):
           os.mkdir('Output/faqCharEndPass')
      if not os.path.isfile('Output/faqCharEndPass/faqCharEndPass.txt'):
           os.system('echo > Output/faqCharEndPass/faqCharEndPass.txt')
      try:
         #good = 0
         #bad = 0
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         cmd =input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Char{Style.RESET_ALL} to Add At The End Of The Password:{Style.RESET_ALL} ")
         with open(burn, mode="r", encoding="utf-8") as myFile:
            lines = myFile.readlines()
            with open('Output/faqCharEndPass/faqCharEndPass.txt', mode="w+", encoding="utf-8") as file1:
               for rows in lines:
                      
                      line = rows.rstrip('\n').split(":")
                      compte = line
                      if len(compte) == 2:
                             pwd = compte[1]
                             pwd = pwd + cmd
                             compte[1] = pwd
                             compte = str(compte).replace("['", "").replace("', '", ":").replace("']", "")
                             file1.write(str(compte) + '\n')
               input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Adding The{Fore.RED} Char{Style.RESET_ALL} At The End Of The Password, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
               menu()
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()

def faqComboDumper():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqDumper'):
           os.mkdir('Output/faqDumper')
      
      
      try:
         #good = 0
         #bad = 0
         #burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         print(f"\n\t{Fore.RED}[{Style.RESET_ALL}1{Fore.RED}] {Style.RESET_ALL}Combo{Fore.RED} 5k{Style.RESET_ALL}{Style.RESET_ALL}")
         print(f"\n\t{Fore.RED}[{Style.RESET_ALL}2{Fore.RED}] {Style.RESET_ALL}Combo{Fore.RED} 25k{Style.RESET_ALL}{Style.RESET_ALL}")
         print(f"\n\t{Fore.RED}[{Style.RESET_ALL}3{Fore.RED}] {Style.RESET_ALL}Combo{Fore.RED} 100k{Style.RESET_ALL}{Style.RESET_ALL}")
         print(f"\n\t{Fore.RED}[{Style.RESET_ALL}4{Fore.RED}] {Style.RESET_ALL}Combo{Fore.RED} Infinity{Style.RESET_ALL}{Style.RESET_ALL}")
         cmd =int(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Option{Style.RESET_ALL}:{Style.RESET_ALL} "))
         if cmd == 1:
                for i in range(16):
                       r = requests.get("https://combolist.org/generate")
                       scrape = r.text.split("<textarea id=combolist spellcheck=false>")[1]
                       dumped = scrape.split("</textarea>")[0]
                       with open("Output/faqDumper/faqCombo 5k.txt","a")as f:
                           f.write(dumped+"\n")
         if cmd == 2:
                for i in range(83):
                       r = requests.get("https://combolist.org/generate")
                       scrape = r.text.split("<textarea id=combolist spellcheck=false>")[1]
                       dumped = scrape.split("</textarea>")[0]
                       with open("Output/faqDumper/faqCombo 25k.txt","a")as f:
                           f.write(dumped+"\n")
         if cmd == 3:
                for i in range(333):
                       r = requests.get("https://combolist.org/generate")
                       scrape = r.text.split("<textarea id=combolist spellcheck=false>")[1]
                       dumped = scrape.split("</textarea>")[0]
                       with open("Output/faqDumper/faqCombo 100k.txt","a")as f:
                           f.write(dumped+"\n")
         if cmd == 4:
                while True:
                       
                        try:
                           r = requests.get("https://combolist.org/generate")
                           scrape = r.text.split("<textarea id=combolist spellcheck=false>")[1]
                           dumped = scrape.split("</textarea>")[0]
                           pass
                        except:
                           print(Fore.RED + "Tool Cannot Start Work !")
                        with open("faqCombo Infinity.txt","a")as esra:
                           esra.write(dumped+"\n")
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Dumping{Fore.RED} Combos{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      except ValueError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}Enter {Fore.RED}Correct{Style.RESET_ALL} Option, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
                        
def faqComboCleaner():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqCleaner'):
           os.mkdir('Output/faqCleaner')
      if not os.path.isfile('Output/faqCleaner/faqGood.txt'):
           os.system('echo > Output/faqCleaner/faqGood.txt')
      if not os.path.isfile('Output/faqCleaner/faqBad.txt'):
           os.system('echo > Output/faqCleaner/faqBad.txt')
      try:
         #good = 0
         #bad = 0
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         faqGood = open('Output/faqCleaner/faqGood.txt', 'w')
         faqBad = open('Output/faqCleaner/faqBad.txt', 'w')
         with open(burn, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                   compte = line.rstrip('\n').split(':')
                   if len(compte) == 2:
                          faqGood.write(":".join(compte) + "\n")
                          #good += 1
                   else:
                         faqBad.write(":".join(compte) + "\n")
                         #bad+=1
            faqBad.close()
            faqGood.close()
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Removing The{Fore.RED} Capture{Style.RESET_ALL} From The File, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()   
      
def faqCaptureRemove():
      clear()
      print(banner)
      if os.path.isdir('Output/faqCaptureRemove'):
           os.system('rmdir /s Output/faqCaptureRemove"' if os.name == 'nt' else 'rm -r Output/faqCaptureRemove')
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqCaptureRemove'):
           os.mkdir('Output/faqCaptureRemove')
      if not os.path.isfile('Output/faqCaptureRemove/faqCaptureRemove.txt'):
           os.system('echo > Output/faqCaptureRemove/faqCaptureRemove.txt')
      
      try:
         combos = []
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         with open(burn, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
               try:
                     combos.append(line.replace('\n', ''))
               except:
                     pass
         for combo in combos:
            try: # Includes at least 2 non whitespace characters, but removes them.
               email = combo.split(':')[0].split(' ')[1]
               password = combo.split(':')[1].split(' ')[0]
               
               with open('Output/faqCaptureRemove/faqCaptureRemove.txt', 'a', encoding='UTF-8') as f:
                  f.write(f'{email}:{password}\n')
            except:
                  try: # Includes non whitespace characters after the password, but removes them.
                        email = combo.split(':')[0]
                        password = combo.split(':')[1].split(' ')[0]

                        with open('Output/faqCaptureRemove/faqCaptureRemove.txt', 'a', encoding='UTF-8') as f:
                           f.write(f'{email}:{password}\n')
                  except:
                        try: # Includes non whitespace characters before the email/username, but removes them.
                           email = combo.split(':')[0].split(' ')[1]
                           password = combo.split(':')[1]

                           with open('Output/faqCaptureRemove/faqCaptureRemove.txt', 'a', encoding='UTF-8') as f:
                              f.write(f'{email}:{password}\n')
                        except: # Clean "combo".
                              if ':' in combo:
                                 with open('Output/faqCaptureRemove/faqCaptureRemove.txt', 'a', encoding='UTF-8') as f:
                                       f.write(f'{combo}\n')
                              else:
                                 pass
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Removing The{Fore.RED} Capture{Style.RESET_ALL} From The File, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
         
def faqCharRemove():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqCharRemove'):
           os.mkdir('Output/faqCharRemove')
      if not os.path.isfile('Output/faqCharRemove/faqCharRemove.txt'):
           os.system('echo > Output/faqCharRemove/faqCharRemove.txt')
      try:
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         cmd =input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Letter{Style.RESET_ALL} to Remove:{Style.RESET_ALL} ")
         with open(burn, 'r') as infile, \
            open(r'Output/faqCharRemove/faqCharRemove.txt', 'w') as outfile:
               for lines in infile:
                      line = lines.replace(cmd, "")
                      outfile.write(line)
               
         
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Removing The{Fore.RED} Char{Style.RESET_ALL} From The File, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
         
def faqDomainChanger():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqDomainChanger'):
           os.mkdir('Output/faqDomainChanger')
      if not os.path.isfile('Output/faqDomainChanger/faqDomainChanger.txt'):
           os.system('echo > Output/faqDomainChanger/faqDomainChanger.txt')
      if not os.path.isfile('Output/faqDomainChanger/faqDomainChangerSpecifique.txt'):
           os.system('echo > Output/faqDomainChanger/faqDomainChangerSpecifique.txt')
      try:
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         print(f"\n\t{Fore.RED}[{Style.RESET_ALL}1{Fore.RED}] {Style.RESET_ALL}Change{Fore.RED} Specifique{Style.RESET_ALL} Domain{Style.RESET_ALL} ")
         print(f"\n\t{Fore.RED}[{Style.RESET_ALL}2{Fore.RED}] {Style.RESET_ALL}Change{Fore.RED} All{Style.RESET_ALL} Domains{Style.RESET_ALL} ")
         cmd =int(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Option{Style.RESET_ALL}:{Style.RESET_ALL} "))
         if cmd == 1:
                domain1 = str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Domain{Style.RESET_ALL} to be changed{Style.RESET_ALL}: "))
                domain2 = str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Domain{Style.RESET_ALL} to change to{Style.RESET_ALL}: "))
                with open(burn, mode="r", encoding="utf-8") as myFile:
                  lines = myFile.readlines()
                  
                  with open('Output/faqDomainChanger/faqDomainChangerSpecifique.txt', mode="w+", encoding="utf-8") as file1:
                     for rows in lines:
                           line = rows.rstrip('\n').split(":")
                           compte = line
                           if len(compte) == 2:
                                 try:
                                    email = compte[0]
                                    psw = compte[1]
                                    email = email.split("@")
                                    user = email[0]
                                    domain = email[1]
                                    if str(domain) == str(domain1):
                                          domain = domain2
                                          email[1] = domain
                                          email = str(email).replace("['", "").replace("', '", "@").replace("']", "")
                                          compte = str(email) + ":"+str(compte[1])
                                          file1.write(str(compte) + '\n')
                                 except IndexError:
                                    pass
                                 
                  input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Changing The{Fore.RED} Domain{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
                  menu()

         elif cmd == 2:
            
               #domain1 = str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Domain{Style.RESET_ALL} to be changed{Style.RESET_ALL}: "))
               domain2 = str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter{Fore.RED} Domain{Style.RESET_ALL} to change to{Style.RESET_ALL}: "))
               with open(burn, mode="r", encoding="utf-8") as myFile:
                 lines = myFile.readlines()
                 
                 with open('Output/faqDomainChanger/faqDomainChanger.txt', mode="w+", encoding="utf-8") as file1:
                    for rows in lines:
                          line = rows.rstrip('\n').split(":")
                          compte = line
                          if len(compte) == 2:
                                try:
                                   email = compte[0]
                                   psw = compte[1]
                                   email = email.split("@")
                                   user = email[0]
                                   domain = email[1]
                                   
                                   domain = domain2
                                   email[1] = domain
                                   email = str(email).replace("['", "").replace("', '", "@").replace("']", "")
                                   compte = str(email) + ":"+str(compte[1])
                                   file1.write(str(compte) + '\n')
                                except IndexError:
                                   pass
                 input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Changing The{Fore.RED} Domain{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
                 menu()
      except:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}Error, Please Enter {Fore.RED}Correct{Style.RESET_ALL} Option And Make Sure The Combo file name is correct, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()    
         
def faqUpperPassword():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqUpperPassword'):
           os.mkdir('Output/faqUpperPassword')
      if not os.path.isfile('Output/faqUpperPassword/faqUpperPassword.txt'):
           os.system('echo > Output/faqUpperPassword/faqUpperPassword.txt')
         
      try:
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         with open(burn, mode="r", encoding="utf-8") as myFile:
            lines = myFile.readlines()
            
            with open("Output/faqUpperPassword/faqUpperPassword.txt", "w+") as f:
               for line in lines:
                     
                     usr = line.split(':')[0]
                     psw = line.split(':')[1]
                     
                     f.write(f'{usr}:{psw.capitalize()}')
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Uppering The{Fore.RED} 1st{Style.RESET_ALL} char of the passwords, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()
      
def faqShuffle():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqShuffle'):
           os.mkdir('Output/faqShuffle')
      if not os.path.isfile('Output/faqShuffle/faqShuffle.txt'):
           os.system('echo > Output/faqShuffle/faqShuffle.txt')
      try:
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         with open(burn, mode="r", encoding="utf-8") as myFile:
            lines = myFile.readlines()
            
         random.shuffle(lines)
         with open('Output/faqShuffle/faqShuffle.txt', 'w+') as f:
            f.writelines(lines)
         
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Shuffling The{Fore.RED} Combo{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqWaterMark():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqWaterMark'):
           os.mkdir('Output/faqWaterMark')
      if not os.path.isfile('Output/faqWaterMark/faqWaterMark.txt'):
           os.system('echo > Output/faqWaterMark/faqWaterMark.txt')
       
      
      
      try:
         burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
         separator =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter the{Fore.RED} custom{Style.RESET_ALL} separator:{Style.RESET_ALL} "))
         author =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Author{Fore.RED}:{Style.RESET_ALL} "))
       
         with open(burn) as combo:
            file = combo.readlines()

         with open('Output/faqWaterMark/faqWaterMark.txt', 'wt') as x:
            for line in file:
                  line = ' '.join([line.strip() for line in line.strip().splitlines() if line.strip()])
                  x.write(f'{line} {separator} {author}\n')
            x.close()
                   
         
               
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Adding{Fore.RED} WaterMark{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqReverse():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqReverse'):
           os.mkdir('Output/faqReverse')
      if not os.path.isfile('Output/faqReverse/faqReverse.txt'):
           os.system('echo > Output/faqReverse/faqReverse.txt')
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         with open(burn) as combo:
            file = combo.readlines()
      
         with open('Output/faqReverse/faqReverse.txt', 'wt') as x:
            for line in file:
                  try:
                     usr = []
                     psw = []
                     splitusr = line.split(':')[0].splitlines()
                     splitpsw = line.split(':')[1].splitlines()
                     usr.append(splitusr)
                     psw.append(splitpsw)
                     
                     x.write(f'{psw[0]}:{usr[0]}\n')
                  except IndexError:
                     pass
            x.close()
         with open('Output/faqReverse/faqReverse.txt', 'rt') as f:
            file = f.readlines()
         with open('Output/faqReverse/faqReversed.txt', 'w+') as wxdf:
            for line in file:
               wxdf.write(line.translate({ ord(c): None for c in "'" }))
            wxdf.close()
         with open('Output/faqReverse/faqReversed.txt', 'r+') as f:
            file = f.readlines()
         with open('Output/faqReverse/faqReversed.txt', 'w+') as wxdf:
            for line in file:
               wxdf.write(line.translate({ ord(c): None for c in "[]" }))
            wxdf.close()
         os.system('del /f "Output/faqReverse/faqReverse.txt"' if os.name == 'nt' else 'rm -r Output/faqReverse/faqReverse.txt')
         
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Converting{Fore.RED} Email to User{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()
      
def faqComboExtractor():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqComboExtractor'):
           os.mkdir('Output/faqComboExtractor')
      if not os.path.isfile('Output/faqComboExtractor/faqComboExtractor.txt'):
           os.system('echo > Output/faqComboExtractor/faqComboExtractor.txt')
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         with open(burn,'rt') as combo:
            with open('Output/faqComboExtractor/faqComboExtractor.txt','wt') as x:
               for line in combo:
                     new_line = line.split(':')[0]+':'+line.split(':')[1].split()[0]
                     x.write(f'{new_line}\n')
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Extracting{Fore.RED} Combo{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqEmailToUser():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqEmailToUser'):
           os.mkdir('Output/faqEmailToUser')
      if not os.path.isfile('Output/faqEmailToUser/faqEmailToUser.txt'):
           os.system('echo > Output/faqEmailToUser/faqEmailToUser.txt')
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         with open(burn,'rt') as combo:
            with open('Output/faqEmailToUser/faqEmailToUser.txt','wt') as x:
               for line in combo:
                     new_line = line.split(':')[0].split('@')[0]+':'+line.split(':')[1]
                     x.write(new_line)
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Converting{Fore.RED} Email to User{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqEmailExtractor():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqEmailExtractor'):
           os.mkdir('Output/faqEmailExtractor')
      if not os.path.isfile('Output/faqEmailExtractor/faqEmailExtracted.txt'):
           os.system('echo > Output/faqEmailExtractor/faqEmailExtracted.txt')
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         with open(burn,'rt') as combo:
            with open('Output/faqEmailExtractor/faqEmailExtracted.txt','wt') as x:
               for line in combo:
                     
                  combo = line.strip().split(':')
                  x.write(combo[0] + '\n')
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finsihed Extracting{Fore.RED} Emails{Style.RESET_ALL} From the Combo, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqChangeSplit():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqSplitChange'):
           os.mkdir('Output/faqSplitChange')
      if not os.path.isfile('Output/faqSplitChange/faqChangedSplit.txt'):
           os.system('echo > Output/faqSplitChange/faqChangedSplit.txt')

      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      split =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter The Current Split{Fore.RED} Char{Style.RESET_ALL}: "))
      new_split =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter The New Split{Fore.RED} Char{Style.RESET_ALL}: "))
      
      try:
         f = codecs.open(burn,encoding='utf-8')
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      contents = f.read()
      newcontents = contents.replace(split,new_split)
      with open('Output/faqSplitChange/faqChangedSplit.txt', 'w') as f:
         f.write(newcontents)
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Changed The{Fore.RED} Split{Style.RESET_ALL} Char, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqCount():
      clear()
      print(banner)
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         num_lines = sum(1 for line in open(burn))
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Combo Length is{Fore.RED} {num_lines}{Style.RESET_ALL} lines, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqSort():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqSort'):
           os.mkdir('Output/faqSort')
      if not os.path.isfile('Output/faqSort/faqSorted.txt'):
           os.system('echo > Output/faqSort/faqSorted.txt')
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         openFile = open(burn, "r") 
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      data=openFile.readlines()
      data.sort()
      with open('Output/faqSort/faqSorted.txt', 'w') as f:
         
         for i in range(len(data)):
            f.write(data[i])
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finished Sorting the{Fore.RED} Combo{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()

def faqDuplicate():
      clear()
      print(banner)
      if not os.path.isdir('Output'):
            os.mkdir('Output')
      if not os.path.isdir('Output/faqDuplicates'):
           os.mkdir('Output/faqDuplicates')
      dup = 0
      burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
      try:
         openFile = open(burn, "r") 
      except FileNotFoundError:
         input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
         menu()
      writeFile = open("Output/faqDuplicates/faqRemovedDuplicates.txt", "w") 
      #Store traversed lines
      tmp = set() 
      for txtLine in openFile: 
      #Check new line
         if txtLine not in tmp: 
            writeFile.write(txtLine) 
      #Add new traversed line to tmp 
            tmp.add(txtLine)
         else:    
                dup+=1
      openFile.close() 
      writeFile.close()
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Removed {Fore.RED}{dup}{Style.RESET_ALL} lines, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()
                    
def faqFilter():
   clear()
   print(banner)

   nb=0
   notmail=0
   Yahoo=0
   Mailru=0
   inboxru=0
   bkru=0
   hotmail=0
   live=0
   outlook=0
   seznamcz=0
   gmail=0
   orangefr=0
   yandex=0
   gmx=0
   TunisienShitt=0
   aol=0
   freefr=0
   rambler=0
   citromailhu=0
   cncom=0
   Freenetde=0
   freemailhu=0
   abv=0
   tonlinede=0
   op=0
   onet=0
   vp=0
   other=0
   
   burn =str(input(f"\n\t{Fore.RED}[{Style.RESET_ALL}@{Fore.RED}] {Style.RESET_ALL}Enter Combo/MailList{Fore.RED} [{Style.RESET_ALL}.txt{Fore.RED}]{Style.RESET_ALL}: "))
   
   if not os.path.isdir('Output'):
        os.mkdir('Output')
   if not os.path.isdir('Output/faqFilter'):
        os.mkdir('Output/faqFilter')
   try:
      with open(burn, 'r') as earth:
         file = earth.read().splitlines()
   except FileNotFoundError:
      input(f"\n\t{Fore.RED}[{Style.RESET_ALL}#{Fore.RED}] {Style.RESET_ALL}File {Fore.RED}Not{Style.RESET_ALL} Found, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
      menu()
   for fade in file:
    fade=fade.lower()
    nb=nb+1
    try:
     if '@' not in str(fade):
        notmail=notmail+1
     elif '@yahoo.' in str(fade):
        Yahoo=Yahoo+1
        zzz=open('Output/faqFilter/yahoo.txt','a')
        zzz.write(fade+'\n')
     elif '@mail.ru' in str(fade):
        Mailru=Mailru+1
     elif  '@inbox.ru' in str(fade):
        inboxru=inboxru+1
        zzz=open('Output/faqFilter/inbox.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@bk.ru' in str(fade):
        bkru=bkru+1
        zzz=open('Output/faqFilter/bk.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@hotmail' in str(fade):
        hotmail=hotmail+1
        zzz=open('Output/faqFilter/hotmail.txt','a')
        zzz.write(fade+'\n')
     elif  '@live' in str(fade):
        live=live+1
        zzz=open('Output/faqFilter/live.txt','a')
        zzz.write(fade+'\n')
     elif  '@outlook' in str(fade):
        outlook=outlook+1
        zzz=open('Output/faqFilter/outlook.txt','a')
        zzz.write(fade+'\n')
     elif '@seznam.cz' in str(fade):
        seznamcz=seznamcz+1
        zzz=open('Output/faqFilter/seznam.cz.txt','a')
        zzz.write(fade+'\n')
     elif '@gmail.com' in str(fade):
        gmail=gmail+1
        zzz=open('Output/faqFilter/gmail.com.txt','a')
        zzz.write(fade+'\n')
     elif '@orange.' in str(fade):
        orangefr=orangefr+1
        zzz=open('Output/faqFilter/orange.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@yandex.' in str(fade):
        yandex=yandex+1
        zzz=open('Output/faqFilter/yandex.txt','a')
        zzz.write(fade+'\n')
     elif '@gmx.' in str(fade):
        gmx=gmx+1
        zzz=open('Output/faqFilter/gmx.txt','a')
        zzz.write(fade+'\n')
     elif '.tn' in str(fade):
        TunisienShitt=TunisienShitt+1
        zzz=open('Output/faqFilter/tona.txt','a')
        zzz.write(fade+'\n')
     elif '@aol.' in str(fade):
        aol=aol+1
        zzz=open('Output/faqFilter/aol.txt','a')
        zzz.write(fade+'\n')
     elif '@free.fr' in str(fade):
        freefr=freefr+1
        zzz=open('Output/faqFilter/free.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@rambler.' in str(fade):
        rambler=rambler+1
        zzz=open('Output/faqFilter/rambler.txt','a')
        zzz.write(fade+'\n')
     elif '@citromail.hu' in str(fade):
        citromailhu=citromailhu+1
        zzz=open('Output/faqFilter/citromail.txt','a')
        zzz.write(fade+'\n')
     elif '@21cn.com' in str(fade):
        cncom=cncom+1
        zzz=open('Output/faqFilter/21cn.com.txt','a')
        zzz.write(fade+'\n')
     elif '@freenet.de' in str(fade):
        Freenetde=Freenetde+1
        zzz=open('Output/faqFilter/freenet.de.txt','a')
        zzz.write(fade+'\n')
     elif '@freemail.hu' in str(fade):
        freemailhu=freemailhu+1
        zzz=open('Output/faqFilter/freemail.hu.txt','a')
        zzz.write(fade+'\n')
     elif '@abv.bg' in str(fade):
        abv=abv+1
        zzz=open('Output/faqFilter/abv.bg.txt','a')
        zzz.write(fade+'\n')
     elif '@t-online.de' in str(fade):
        tonlinede=tonlinede+1
        zzz=open('Output/faqFilter/t.online.txt','a')
        zzz.write(fade+'\n')
     elif '@op.' in str(fade):
        op=op+1
        zzz=open('Output/faqFilter/op.txt','a')
        zzz.write(fade+'\n')
     elif '@onet.' in str(fade):
        onet=onet+1
        zzz=open('Output/faqFilter/onet.txt','a')
        zzz.write(fade+'\n')
     elif '@vp' in str(fade):
        vp=vp+1
        zzz=open('Output/faqFilter/vp.txt','a')
        zzz.write(fade+'\n')
     else:
        other=other+1
        zzz=open('Output/faqFilter/other.txt','a')
        zzz.write(fade+'\n')
    except:
       pass
   input(f"\n\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}] {Style.RESET_ALL}Finished Filtering Emails By{Fore.RED} Domains{Style.RESET_ALL}, Press Any {Fore.RED}Key{Style.RESET_ALL} To Continue...")
   menu()

menu()