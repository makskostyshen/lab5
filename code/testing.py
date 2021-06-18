from sys import argv
import json
import csv
import re
#C:\Users\maxxx\Documents\GitHub\lab5\task0.ini


class First:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __eq__(self, other):
        return self.arg1 == other.arg1

    def __str__(self):
        return f"{self.arg1}"

class Second(First):
    def __init__(self, arg1):
        self.arg1 = arg1

c = First(1, 2)
print(c)
d = Second(2)
print(d)
print(c==d)




