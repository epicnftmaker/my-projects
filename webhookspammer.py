"""
made by epicnftmaker
"""
print("""
                                                                                                 
                         _                            _        
                       (_)               _          | |       
 ____    ____   ___     _   ____   ____ | |_      _ | | _ _ _ 
|  _ \  / ___) / _ \   | | / _  ) / ___)|  _)    / || || | | |
| | | || |    | |_| |  | |( (/ / ( (___ | |__   ( (_| || | | |
| ||_/ |_|     \___/  _| | \____) \____) \___)   \____| \____|
|_|                  (__/                                                          
                                    Made by epicnftmaker
                                  Github: epicnftmaker
""")

from dhooks import Webhook
import time
import colorama
from colorama import Fore, Style, Back
colorama.init()

def menu():
    print("[1] delete webhook")
    print("[2] spam webhook")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        webhookurl = Webhook(input("paste the webhook here: "))
        webhookurl.delete()  
        print("deleted")
        exit()
    elif option == 2:
        message = input("what do you want to spam : ")
        webhookurl = Webhook(input("enter webhook  its not hard: "))   
        modify = input("what do you want the name to be of the webhook")
        webhookurl.modify(name=modify)
    while True:
        webhookurl.send('https://discord.gg/projectwd powered by epicnftmaker ' + message)
        print(Fore.GREEN + "Sent.")
    
         


menu()
option = int(input("Enter your option: "))
