import re


def validate_code(code: str) -> bool:

    valid_code = re.compile(r"^[A-Z]{2,4}\d{4}$")

    return bool(valid_code.match(code))


def validate_semester(semester: str) -> bool:

    valid_semester = re.compile(
        r"^(Fall|Spring|Summer) 20\d{2}$"
    )

    return bool(valid_semester.match(semester))


def validate_grade(grade: str) -> bool:

    valid_grades = [
        'A+', 'A', 'A-',
        'B+', 'B', 'B-',
        'C+', 'C', 'C-',
        'D+', 'D', 'D-',
        'F'
    ]

    return grade in valid_grades
