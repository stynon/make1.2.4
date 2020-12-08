#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import
import os

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def com_mana():
    com_input = input("""
--------------------------------------------------
|1: Disk space   | 4: List open files            |
|2: Ram use      | 5: Network packets statistics | 
|3: Disk manager | 6: Monitor network trafric    |
--------------------------------------------------
Please enter your choice (q to go back): """)

    if com_input == "1":
        os.system("df -h")
        com_mana()
    elif com_input == "2":
        os.system("free -h")
        com_mana()
    elif com_input == "3":
        os.system("sudo cfdisk")
        com_mana
    elif com_input == "4":
        os.system("sudo lsof | more")
        os.system("clear")
        com_mana()
    elif com_input == "5":
        os.system("netstat -a | more")
        os.system("clear")
        com_mana()
    elif com_input == "6":
        os.system("sudo nethogs")
        os.system("clear")
        com_mana()
    elif com_input == "Q" or com_input == "q":
        os.system("clear")
        menu()
    else:
        os.system("clear")
        print(29 * "-")
        print("|You must only select option|")
        print("|Please try again           |")
        print(29 * "-")
        com_mana()

