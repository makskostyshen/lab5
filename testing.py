from sys import argv
import json
import csv



#with open(r'C:\Users\maxxx\Documents\GitHub\lab5\task0.ini') as f:
#    d = json.load(f)
#    print (d)

#C:\Users\maxxx\Documents\GitHub\lab5\task0.ini

d = {'7': 9, "6": 87, "90": {"5": 34, "6": 8}}
print(d['90']['5'])

print(d.get('6').get('9'))