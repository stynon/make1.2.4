#!/usr/bin/env python
"""
Een python script dat random wachtwoorden genereert.
zowel kleine letters als grote, cijfers en tekens
op aanvraag de complexiteit (aantal tekens en soort tekens)
maak gebruik van flowcontrol en functies!
"""

# Import
import random
import string


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def passwordgenerator():
    password_length = int(input("How long does your password need to be?\n"))
    password_char = string.ascii_letters + string.digits + string.punctuation
    password = []
    for x in range(password_length):
        password.append(random.choice(password_char))
    print("". join(password))
