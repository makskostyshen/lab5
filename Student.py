"""created by Kostyshen Maksym"""

from Skips import Skips

class Student:
    def __init__(self, sname, name, course=None, group=None):
        self._sname = sname
        self._name = name
        self._course = course
        self._group = group
        self._total_skips = 0
        self._lecture_skips = 0
        self._skips = []

    @property
    def sname(self):
        return self._sname

    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course

    @property
    def group(self):
        return self._group

    @property
    def total_skips(self):
        return self._total_skips

    @property
    def lecture_skips(self):
        return self._lecture_skips

    def add_skip(self, subj, day, pair, audi, type, week):

        new = Skips(subj, day, pair, audi, type, week)
        self._skips.append(new)
        return new

    def load_skip(self, subj, day, pair, audi, type, week):
        self._total_skips+=1
        if(type == "Lecture"):
            self._lecture_skips+=1
        skip = self.add_skip(subj, day, pair, audi, type, week)
        return skip

    def __eq__(self, other):
        return ((other.sname == self.sname) & (other.name == self.name))

    def __repr__(self):
        return f"({self.sname}, {self._skips}, lec={self._lecture_skips}, total={self._total_skips})"
        #prosto shcob bachyty
    def __str__(self):
        return f"({self.sname}, {self._skips}, lec={self._lecture_skips}, total={self._total_skips})"


lis = ["ssmaks", "maks", "1", "krovi"]

s = Student(*lis)



#print(s.sname)
#
#
#for s in lis:
#    if(s=="1"):
#        break
#        print(s)
#        print(3)
#    print(s)
#    print(3)