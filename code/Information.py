"""

This module contains class Information, which contains all data and knows how to output it:

created by Kostyshen Maksym
"""

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


    def _output(self, file) -> None:
        results = self.result_list()                            ##

        for res in results:
            file.write(f"pairs skipped: {res['skipped_p']}\tlectures skipped:{res['skipped_l']}"
                       f"\t{res['stud'].sname}\t{res['stud'].name}\n")

            for sk in res["skips"]:
                file.write(f"\t{sk.subject}\t{sk.type}\t{res['stud'].get_count_of_skips_by_type(sk.type)}\n")


    def result_list(self) -> list:
        """
        Check students and return the list with needed information of students to output
        """

        students = []
        for student in self._students:

            if (lecture_sk := student.lecture_skips) > 15:

                obj = {
                    "stud": student,
                    "skipped_p": student.total_skips,
                    "skipped_l": lecture_sk,
                    "skips": student.get_all_sorted_skips()
                }

                students.append(obj)
        return students


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
        """
        Load all data.

            input:
                subject, sname, day, pair, auditory,
                type, week, course, group, name - all data.

            output:
                skip - Skips object with required data.

        """

        if (founded:=self.find(sname, name)):
            student = founded
        else:
            student = self.add_student(sname, name, course, group)

        skip = student.load_skip(subject, day, pair, auditory, type, week)
        return skip


    def _summing(self, skip):
        self._total_skips+=1
        if((checking:=skip.auditory) > self.max_auditory):
            self._max_auditory = checking


    def load_data(self, subject, sname, day, pair, auditory,
            type, week, course, group, name):
        skip = self.load_skip(subject, sname, day, pair, auditory,
            type, week, course, group, name)
        self._summing(skip)


    def __str__(self):
        return(f"Object with skips: total skips = {self.total_skips},"
               f"max auditory = {self.max_auditory}")






