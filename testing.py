from sys import argv
import json
import csv
import re

p = re.compile(r"\S[\da-zA-Zа-яА-Я-`]{,2}\S")
#C:\Users\maxxx\Documents\GitHub\lab5\task0.ini


print(re.fullmatch(p, "a-4").group())


a = 1 < 3 < 4
print(a)