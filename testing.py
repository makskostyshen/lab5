from sys import argv
import json
import csv
import re

p = re.compile(r"\S[\da-zA-Zа-яА-Я-`]{,2}\S")
#C:\Users\maxxx\Documents\GitHub\lab5\task0.ini


print(re.fullmatch(p, "a-4").group())


a = {"da" :"net", "as": 7}
b = {"da" :"nit", "as": 7}
c = {"da" :"noo", "as": 7}
d = {"da" :"nou", "as": 7}
e = {"da" :"nii", "as": 7}

l = [a, b, c, d, e]

l.sort(key=lambda as: (as["da"]))
