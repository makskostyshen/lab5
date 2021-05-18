"""created by Kostyshen Maksym"""



class Skips:
    def __init__(self, subject, day, pair, auditory, type, week):
        self._subject = subject
        self._type = type
        self._week = week
        self._day = day
        self._pair = int(pair)
        self._auditory = int(auditory) # need a change

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

    def __repr__(self): #shob bulo
        return f"[{self._subject}, {self._type}, {self._week}, {self._day}, {self._pair}, {self._auditory}]"
