"""created by Kostyshen Maksym"""



class Skips:
    def __init__(self, subj, day, pair, audi, type, week):
        self._subj = subj
        self._type = type
        self._week = week
        self._day = day
        self._pair = int(pair)
        self._audi = int(audi)

    @property
    def subj(self):
        return self._subj

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
    def audi(self):
        return self._audi

    def __repr__(self): #shob bulo
        return f"[{self._subj}, {self._type}, {self._week}, {self._day}, {self._pair}, {self._audi}]"
