#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import
import platform

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def sysinfo():
    # Architecture
    print("Architecture: " + platform.architecture()[0])

    # machine
    print("Machine: " + platform.machine())

    # node
    print("Node: " + platform.node())

    # system
    print("System: " + platform.system())

    # distribution
    dist = platform.dist()
    dist = " ".join(x for x in dist)
    print("Distribution: " + dist)
