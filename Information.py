"""created by Kostyshen Maksym"""

from Student import Student

class Information:

    def __init__(self):
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


    def output(self, output_file, encoding) -> None:
        """
        Output information from object with data to file

        input:

            output_file - file to output into
            encoding - file's encoding
        """

        with open(output_file, "w", encoding=encoding) as output_path:
            self._output(output_path)

    def _prekol(self):
        for stud in self._students:

            stud._skips.sort(key=lambda sorting: ("Lecture", "практ.", "8", "Лаб."))

        for stud in self._students:
            print(stud)

    #def _output(self, output_path):
    #    self._students.sort(key=lambda sorting: ())




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
        #print(f"{self}")
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
        self._prekol()


    def __str__(self):
        return(f"maxau = {self._max_auditory}, total = {self._total_skips}, {self._students}")





