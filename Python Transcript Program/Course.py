class Course:

    def __init__(self, crs_code, crs_semester, crs_grade):

        self.crs_code = crs_code
        self.crs_semester = crs_semester
        self.crs_grade = crs_grade


    # ACCESSOR METHODS

    def get_crs_code(self):
        return self.crs_code

    def get_crs_semester(self):
        return self.crs_semester

    def get_crs_grade(self):
        return self.crs_grade


    # MUTATOR METHODS

    def set_crs_semester(self, new_semester):
        self.crs_semester = new_semester

    def set_crs_grade(self, new_grade):
        self.crs_grade = new_grade


    # STRING METHOD

    def __str__(self):

        out_str = "{:<8}\t{:<12}\t{:<2}"

        return out_str.format(
            self.crs_code,
            self.crs_semester,
            self.crs_grade
        )
