class Builder:


    def __init__(self):
        self._subject = None
        self._sname = None
        self._day = None
        self._pair = None
        self._auditory = None
        self._type = None
        self._week = None
        self._course = None
        self._group = None
        self._name = None


    with open(source) as file:
        csv_object = csv.reader(file)
        for row in csv_object:
            if row: pass

    def _convert_row(self):
        cond1 = isinstance(self._day, int)
        cond2 = isinstance(self._pair, int)
        cond3 = isinstance(self._auditory, int)
        cond4 = isinstance(self._week, int)
        cond5 = isinstance(self._course, int)
        if not (cond1 & cond2 & cond3 & cond4 & cond5):
            raise ValueError

        self._day = int(self._day)
        self._pair = int(self._pair)
        self._auditory = int(self._auditory)
        self._week = int(self._week)
        self._course = int(self._course)
        return self

