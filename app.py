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
        "\n[2] Request OTP Code" +
        "\n[3] Request Password"  +
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
    again = 1
    while(again == 1):
        clear()
        print(".::Purchase Package Menu::.")
        msisdn = str(input("Input your MSISDN >> "))
        po = str(input("Input your OTP >> "))
        print(".::Service ID List::.\n\
8110577 >> Xtra Kuota, 30GB, 30hr, 10K\n\
8210886 >> Xtra Combo Lite 25GB, 30hr, 99.900K\n\
8210885 >> Xtra Combo Lite 17GB, 30hr, 79.900K\n\
8210884 >> Xtra Combo Lite 9GB, 30hr, 49.900K\n\
8210883 >> Xtra Combo Lite 5GB, 30hr, 29.900K\n\
8210882 >> Xtra Combo Lite 3GB, 30hr, 19.900K\n\
8211183 >> Combo Xtra 5GB+5GB, 30hr,59rb\n\
8211184 >> Combo Xtra 10GB+10GB, 30hr, 89rb\n\
8211185 >> Combo Xtra 15GB+15GB, 30hr,129rb\n\
8211231 >> XL GO IZI 10 GB, 7hr, Rp0\n\
NB:the above list can not be used if replaced by the provider.")
        serviceid = str(input("Input your Service ID >> "))
        xl = XL(msisdn)
        r = xl.loginWithOTP(po)
        if(r != False):
            print(xl.purchasePackage(serviceid)['message'])
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            again = 0 if(decision == 'N' or 'n') else again
        else:
            print("Login failed try again")
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()


def menu_2():
    again = 1
    while(again == 1):
        clear()
        print(".::OTP Code Menu::.")
        msisdn = str(input("Input your MSISDN >> "))
        xl = XL(msisdn)
        print(xl.reqOTP()['message'])
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()

def menu_3():
    again = 1
    while(again == 1):
        clear()
        print(".::Password Menu::.")
        msisdn = str(input("Input your MSISDN >> "))
        xl = XL(msisdn)
        print(xl.reqPassword()['message'])
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        again = 0 if(decision == 'N' or 'n') else again
    menu_actions['main']()

def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "3" : menu_3,
    "0" : exit
}


if __name__ == "__main__":
    main_menu()
