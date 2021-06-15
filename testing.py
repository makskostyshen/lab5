from sys import argv
import json
import csv
import re


p = re.compile(r"\S[\da-zA-Zа-яА-Я-`]{,2}\S")

_type_pat3 = "Lecture|практ.|8|Лаб."
_type_pat1 = re.compile("Lecture|практ.|8|Лаб.")
_type_pat4 = re.compile(_type_pat3)
_week_limit = 18
_low_limit = 1
_lecture = "Lecture"
_practice = "практ."
_seminar = "8"
_laboratory = "Лаб."
_type_pat1 = re.compile(_lecture +"|"+ _practice +"|"+ _seminar +"|"+ _laboratory)

#print(_type_pat2, _type_pat3)
print(_type_pat1, _type_pat4)
#C:\Users\maxxx\Documents\GitHub\lab5\task0.ini