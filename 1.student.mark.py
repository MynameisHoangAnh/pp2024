def num_students():
    while True:
        num_students = int(input("Input number of students: "))
        if num_students>0:
            return num_students
        else:
            print("Please enter a correct number of students!!!!")


def student_info():
    students = []  #List of tuples of students 
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        student_info = (student_id, name, dob)
        students.append(student_info)
    return students

def num_courses():
    while True:
        num_courses = int(input("Input number of courses: "))
        if num_courses>0:
            return num_courses
        else:
            print("Please enter a correct number of courses!!!!")


def course_info():
    courses = {} #Use dictionary to help find course using course id is easier :)
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses[course_id] = name
    return courses

def marks_for_course(students, courses):
    course_id = input("Enter the course ID to input marks for: ")
    course_marks = {} #Use dictionary to store marks in format key:value - student id:mark
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} in {courses[course_id]}: "))  # format of tuple students[student id, name, dob] -> student[1] is name
        course_marks[student[0]] = mark  #student[0] to take student's name 
    return course_marks

def list_students(students):
    print("Avalible student/students: ")
    for student_id, name, dob in students:
        print(f"- ID: {student_id}, Name: {name}, Date of Birth: {dob}")

def list_courses(courses):
    print("Avalible course/courses:")
    for course_id, name in courses.items():
        print(f"- {course_id}: {name}")

def show_student_marks(course_marks):
    print("Students's marks for course:")
    for student_id, mark in course_marks.items():
        print(f"- {student_id}: {mark}")


num_students = num_students()
students = student_info()
num_courses = num_courses()
courses = course_info()
course_marks = marks_for_course(students, courses)

list_students(students)
list_courses(courses)
show_student_marks(course_marks)