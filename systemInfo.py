#!/usr/bin/env python
"""
System info weergave
"""

# Import
import platform

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def sysinfo():
    print('system   :', platform.system())
    print('node     :', platform.node())
    print('release  :', platform.release())
    print('version  :', platform.version())
    print('machine  :', platform.machine())
    print('processor:', platform.processor())
