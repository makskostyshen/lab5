"""created by Kostyshen Maksym"""

import re

class Skips:
    _subject_pattern = re.compile(r"\S[\d 'a-zA-Zа-яА-Я-`]{4,22}\S")
    _day_limit = 5
    _pair_limit = 4
    _type_pat = re.compile(r"Lecture|практ.|8|Лаб.")
    _week_limit = 18
    _low_limit = 1


    def __init__(self, subject, day, pair, auditory, type, week):
        self._subject = subject
        self._type = type
        self._week = week
        self._day = day
        self._pair = pair
        self._auditory = auditory

    @property
    def subject(self):
        return self._subject

    @property
    def type(self):
        return self._type

    @property
    def week(self):
        return self._week

    @property
    def day(self):
        return self._day

    @property
    def pair(self):
        return self._pair

    @property
    def auditory(self):
        return self._auditory

    def _check_data(self):

        cond1 = re.fullmatch(self._subject_pattern, subject)
        cond2 = re.fullmatch(self._type_pattern, type)
        cond3 = self._low_limit <= day <= self._day_limit
        cond4 = self._low_limit <= pair <= self._pair_limit


    def __repr__(self): #shob bulo
        return f"[{self._subject}, {self._type}]"
