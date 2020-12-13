"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""


class InputOutString(object):
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input()

    def printString(self):
        print(self.s.upper())


s.Obj = InputOutString()
s.Obj.getString()
s.Obj.printString()
