#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import
import os


__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


# Function to update the system
def updatesystem():
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("clear")

