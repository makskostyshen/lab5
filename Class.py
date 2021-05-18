"""created by Kostyshen Maksym"""

from Student import Student

class Information:

    def __init__(self, subject, sname, day, pair, auditory,
                type, week, course, group, name):
        self._students = []
        self._max_auditory = 0
        self._total_skips = 0

    @property
    def max_auditory(self):
        return self._max_auditory

    @property
    def total_skips(self):
        return self._total_skips

    def clear(self):
        self._students = []
        self._max_auditory = 0
        self._total_skips = 0


    def output(self): pass


    def add_student(self, sname, name, course, group):
        new = Student(sname, name, course, group)
        self._students.append(new)
        return new


    def find(self, sname, name):
        needed = Student(sname, name)
        equal = None
        limit = len(self._students)

        for i in range(limit):
            if (self._students[i] == needed):
                equal = self._students[i]
        return equal

        
    def load_skip(self, subject, sname, day, pair, auditory,
            type, week, course, group, name):

        if (founded:=self.find(sname, name)):
            student = founded
        else:
            student = self.add_student(sname, name, course, group)

        skip = student.load_skip(subject, day, pair, auditory, type, week)
        print(f"{self}")
        return skip

    def summing(self, skip):
        self._total_skips+=1
        if((checking:=skip.auditory) > self.max_auditory):
            self._max_auditory = checking


    def load_data(self, subject, sname, day, pair, auditory,
            type, week, course, group, name):
        skip = self.load_skip(subject, sname, day, pair, auditory,
            type, week, course, group, name)
        self.summing(skip)


    def __str__(self):
        return(f"maxau = {self._max_auditory}, total = {self._total_skips}, {self._students}")






studlist = ["subject", "surname", "day", "pair", "kind", "auditory", "week", "course", "group", "name"]
s1 = ["algebr","Kostyshen","1","4","2","Lecture","1","1","a-4","Maksim"]
s2 = ["algebr","Kostyshena","1","4","1","Lecture","1","1","a-4","Maksim"]
s3 = ["algeb","Kostyshen","1","4","4","Lecture","1","1","a-4","Maksim"]
s4 = ["algeb","Kostyshen","1","4","7","Lecture","1","1","a-4","Maksim"]
c = Information(*studlist)

#c.add("Kostyshen", "maks", "12", "32")
#c.add("Kostyshena", "maks", "12", "32")
#c.add("Kostyshen", "maks", "23", "45")
#c.add("Kos", "maks", "23", "45")
#c.add("Kostysheno", "maks", "23", "45")

#print(c._students[0]==c._students[1])

c.load_data(*s1)
c.load_data(*s2)
c.load_data(*s3)
c.load_data(*s4)

#print(c.find("Kostysheno", "maks"))