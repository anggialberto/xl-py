# -*- coding: utf-8 -*-
import os
import sys
import platform
from xlpy import *

def main_menu():
    clear()
    print(
        "   .::XL - Direct Purchase Package::." +
        "\nPlease choose the menu you want to start:"
        "\n[1] Purchase Package" + 
        "\n[2] Request OTP"  +
        "\n[0] Quit"
    )
    choice = str(input(" >> "))
    exec_menu(choice)
    return

def exec_menu(choice):
    clear()
    if(choice == ''):
        menu_actions['main']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main']()
    return

def menu_1():
    print(".::Purchase Package Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    passwd = str(input("Input your Password >> "))
    print(
        "List of Internet package Service ID:"
        "\n[1] Combo Lite 3GB  - 8211010" + 
        "\n[2] Combo Lite 5GB  - 8211011" +
        "\n[3] Combo Lite 9GB  - 8211012" +
        "\n[4] Combo Lite 17GB - 8211013" +
        "\n[4] Combo Lite 25GB - 8211014" +
        "\n[5] XtraKuota 30GB (Rp. 10.000) - 8110577" +
        "\n-----------------------------------------"
        )
    serviceid = str(input("Input your Service ID >> "))
    xl = XL(msisdn)
    r = xl.loginWithOTP(passwd)
    if(r != False):
        print(xl.purchasePackage(serviceid)['message'])
    else:
        print("Login failed try again")
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['1']()
    return
        
def menu_2():
    clear()
    print(".::Password Menu::.")
    msisdn = str(input("Input your MSISDN >> "))
    xl = XL(msisdn)
    print(xl.reqOTP()['message'])
    decision = str(input("Want to repeat the process [Y/N]? >> "))
    menu_actions['main']() if(decision in ['N','n']) else menu_actions['2']()
    return

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
