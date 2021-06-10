"""created by Kostyshen Maksym"""

from Skips import Skips
import re

class Student:

    _names_pattern = re.compile(r"\S[a-zA-Zа-яА-Я-`]{4,18}\S")
    _group_pattern = re.compile(r"\S[\da-zA-Zа-яА-Я-`]{,2}\S")
    _course_limit = 4
    _low_limit = 1


    def __init__(self, sname, name, course=None, group=None):
        if (course and group):
            self._check_data(sname, name, course, group)

        self._sname = sname
        self._name = name
        self._course = course
        self._group = group
        self._total_skips = 0
        self._lecture_skips = 0
        self._skips = []

    def get_all_skips(self):
        return self._skips

    def get_count_of_skips_by_type(self, type):
        res = 0
        for subj in self._skips:
            if subj.type == type:
                res += 1
        return res

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

    @staticmethod
    def lecture_name():
        return "Lecture"


    def _check_data(self, sname, name, course, group):

        cond1 = re.fullmatch(self._names_pattern, sname)
        cond2 = re.fullmatch(self._names_pattern, name)
        cond3 = re.fullmatch(self._group_pattern, group)
        cond4 = self._low_limit <= course <= self._course_limit


        if not (cond1 and cond2 and cond3 and cond4):
            raise Exception



    def add_skip(self, subject, day, pair, auditory, type, week):

        new = Skips(subject, day, pair, auditory, type, week)
        self._skips.append(new)
        return new

    def load_skip(self, subject, day, pair, auditory, type, week):
        self._total_skips+=1
        if(type == Student.lecture_name()):
            self._lecture_skips+=1
        skip = self.add_skip(subject, day, pair, auditory, type, week)
        return skip

    def __eq__(self, other):
        return ((other.sname == self.sname) & (other.name == self.name))

    def __repr__(self):
        return f"({self.sname}, {self._skips})"
        #prosto shcob bachyty
    def __str__(self):
        return f"({self.sname}, {self._skips}, lec={self._lecture_skips}, total={self._total_skips})"
