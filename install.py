#!/usr/bin/env python
"""
Software installatie
"""

# Import
import os

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def installvpn():
    os.system("sudo apt-get install openvpn")