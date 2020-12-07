#!/usr/bin/env python
"""
System update en upgrade (linux)
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

