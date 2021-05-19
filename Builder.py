import csv
import re
from Information import Information


class Builder:

    _int_pattern = re.compile("[\d]*")


    def __init__(self, csv_object: csv.reader):

        self._object = csv_object
        self._current = None


    @property
    def current(self):
        return self._current


    @staticmethod
    def fields_number():
        return 10


    def load_data(self, holder: Information):

        #print(type(self))
        for row in self._object:
            if row:
                self.row_proceed(row)
                holder.load_data(self._current["subject"], self._current["sname"], self._current["day"],
                                 self._current["pair"], self._current["auditory"], self._current["type"],
                                 self._current["week"], self._current["course"], self._current["group"],
                                 self._current["name"])


    def row_proceed(self, row):


        if (len(row) != self.fields_number):
            #raise Exception
            #                                        !!!!!!!!!!!!!!!!!!!!!!
            print("ok")
        keys = ["subject", "sname", "day", "pair", "auditory", "type", "week", "course", "group", "name"]
        data = {keys[i] : row[i] for i in range(len(keys))}
        self._check_int(data)
        self._current = self._convert_row(data)
        #print(self.current)


    def _check_int(self, data):
        re.fullmatch(self._int_pattern, data["day"]).group()
        re.fullmatch(self._int_pattern, data["pair"]).group()
        re.fullmatch(self._int_pattern, data["auditory"]).group()
        re.fullmatch(self._int_pattern, data["week"]).group()
        re.fullmatch(self._int_pattern, data["course"]).group()



    def _convert_row(self, data):
        data["day"] = int(data["day"])
        data["pair"] = int(data["pair"])
        data["auditory"] = int(data["auditory"])
        data["week"] = int(data["week"])
        data["course"] = int(data["course"])
        #print(data["course"])
        #print(type(data["course"]))
        return data


    def __str__(self):
        return f"{self.current()}"


#with open("infor.csv", encoding="utf-8") as file:
#    r = csv.reader(file)
#    info = Builder(r)
#    holder = Information()
#    info.load(holder)
