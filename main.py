#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import
import datetime
import os
import sys
import passwordgen
import updateSystem
import ifConfig
import systemInfo
import install
#import networkscan
import portscan

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def restart():
    menu()


def menu():
    now = datetime.datetime.now()
    print(now.strftime("[%H:%M]"), 3 * "-", "Control Center", 10 * "-")
    choice = input("""
    1: Ip weergave       | 5: Networkscan               | 9:  Apparmor
    2: PasswordGen       | 6: System update en upgrade  | 10: Computer management
    3: System info       | 7: Portscan
    4: Install openvpn   | 8: Firewall
""")

    if choice == "1":
        ifConfig.ip()
        restart()
    elif choice == "2":
        passwordgen.passwordgenerator()
        restart()
    elif choice == "3":
        systemInfo.sysinfo()
        restart()
    elif choice == "4":
        install.installvpn()
        restart()
    elif choice == "5":
        c=2
    elif choice == "6":
        updateSystem.updatesystem()
    elif choice == "7":
        portscan.port()
        restart()
    elif choice == "8":
        x = 1
    elif choice == "9":
        x=1
    elif choice == "10":
        x=1
    else:
        print(29 * "-")
        print("|You must only select option|")
        print("|Please try again           |")
        print(29 * "-")
        menu()


if __name__ == '__main__':  # code to execute if called from command-line
    menu()