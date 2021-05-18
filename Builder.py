import csv

class Builder:
    def __init__(self, csv_object: csv.reader):
        self._object = csv_object
        self._current = next(self._object)
        print(self._object, self._current)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._object)




with open("infor.csv", encoding="utf-8") as file:
    r = csv.reader(file)
    for i in Builder(r):
        print(file)
    #readdd = csv.reader(file)
    #print(next(readdd))
    #print(next(readdd))
    #print(next(readdd))
    #print(next(readdd))
    #print(next(readdd))



