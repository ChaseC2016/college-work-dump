from Course import Course
from validations import (
    validate_code,
    validate_semester,
    validate_grade
)


def add_course(transcript):

    valid = False

    while valid == False:

        code = input("Enter course code: ")

        valid = validate_code(code)

        if valid == False:
            print("Invalid course code.")

    valid = False

    while valid == False:

        semester = input("Enter semester: ")

        valid = validate_semester(semester)

        if valid == False:
            print("Invalid semester.")

    valid = False

    while valid == False:

        grade = input("Enter grade: ")

        valid = validate_grade(grade)

        if valid == False:
            print("Invalid grade.")

    new_course = Course(
        code,
        semester,
        grade
    )

    transcript.append(new_course)

    print("Course Added.\n")


def list_courses(transcript):

    print("\nCourses:\n")

    for course in transcript:
        print(course)


def calculate_GPA(transcript):

    quality_pts = {
        'A+':4.0, 'A':4.0, 'A-':3.67,
        'B+':3.33, 'B':3.0, 'B-':2.67,
        'C+':2.33, 'C':2.0, 'C-':1.67,
        'D+':1.33, 'D':1.0, 'D-':0.67,
        'F':0.0
    }

    tot_hours = 0
    tot_points = 0

    for course in transcript:

        hours = int(course.get_crs_code()[-1])

        points = (
            quality_pts[course.get_crs_grade()]
            * hours
        )

        tot_hours += hours
        tot_points += points

    if tot_hours == 0:
        return 0

    return tot_points / tot_hours


def main():

    transcript = []

    option = 0

    while option != 4:

        print("\n1. Add Course")
        print("2. List Courses")
        print("3. Calculate GPA")
        print("4. Exit")

        option = int(input("Select Option: "))

        if option == 1:
            add_course(transcript)

        elif option == 2:
            list_courses(transcript)

        elif option == 3:

            gpa = calculate_GPA(transcript)

            print(f"\nCurrent GPA: {gpa:.2f}")

        elif option == 4:
            print("Goodbye.")

        else:
            print("Invalid Option.")


main()
