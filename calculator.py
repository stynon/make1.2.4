#!/usr/bin/env python
"""
Je aangepaste rekenmachine die nu volledig aangepast/verbeterd is met de juiste imports, functies en flowcontrol.
"""

#import

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


#Define add
def add(x, y):
    return x + y


#Define substract
def subtract(x, y):
    return x - y


#Define multiply
def multiply(x, y):
    return x * y


#Define divide
def divide(x, y):
    return x / y


def calc():
    #Ask wich calculation needs to happen.
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            #do the add
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            #do the substract
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            #do the multiply
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            #do the divide
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("Invalid Input")

