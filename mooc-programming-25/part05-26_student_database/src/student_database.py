# Write your solution here
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = []


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    print(f"{name}:")
    if len(students[name]) == 0:
        print(" no completed courses")
    else:
        points = 0
        print(f" {len(students[name])} completed courses:")
        for course in students[name]:
            print(f"  {course[0]} {course[1]}")
        for course in students[name]:
            points += int(course[1])
        gpa = float(points / len(students[name]))
        print(f" average grade {gpa}")


def add_course(students: dict, name: str, course: tuple):
    if int(course[1]) == 0:
        return
    for prev_course in students[name]:
        if course[0] == prev_course[0]:
            if int(prev_course[1]) > int(course[1]):
                return
            if int(prev_course[1]) < int(course[1]):
                students[name].remove(prev_course)
                students[name].append(course)
                return
    students[name].append(course)


def summary(students: dict):
    print(f"students {len(students)}")
    most_courses = ""
    courses = 0
    for name in students:
        if len(students[name]) > courses:
            courses = len(students[name])
            most_courses = name
    print(f"most courses completed {courses} {most_courses}")

    gpa = {}

    for name in students:
        points = 0
        for course in students[name]:
            points += int(course[1])
        average = float(points / len(students[name]))
        gpa[name] = average

    best_avg = ""
    avg = 0

    for name, average in gpa.items():
        if average > avg:
            avg = average
            best_avg = name
    print(f"best average grade {avg} {best_avg}")
