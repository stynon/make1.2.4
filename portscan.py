#!/usr/bin/env python
"""
Info about our project comes here.
"""

# Import
from socket import *
import time

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def port():
    startTime = time.time()
    target = input('Enter the host to be scanned: ')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
    print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
    port()