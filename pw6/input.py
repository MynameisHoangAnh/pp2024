import domains.student as student
import domains.course as course
from domains.student import Student, input_student_info
from domains.course import Course, input_course_info

def save_students(students, file_path):
    with open(file_path, "a") as f:
        for student in students:
            f.write(student.to_string() + "\n")

def save_courses(courses, file_path):
    with open(file_path, "a") as f:
        for course in courses:
            f.write(course.to_string() + "\n")

def save_marks(marks, file_path):
    with open(file_path, "a") as f:
        for student_id, course_id, mark in marks.items():
            f.write(f"{student_id},{course_id},{mark}\n")

def input_and_save_students(school):
    students = []
    while True:
        if not input_student_info(students):
            break
    save_students(students, "students.txt")  # Optional text backup

def input_and_save_courses(school):
    courses = []
    while True:
        if not input_course_info(courses):
            break
    save_courses(courses, "courses.txt")  # Optional text backup



def input_students(school):
    num_students = int(input("Input number of students: "))
    for _ in range(num_students):
        student = Student("", "", "")  # Create empty student object
        student.input_info()
        school.self.add_student(student)

def input_courses(school):
    num_courses = int(input("Input number of courses: "))
    for _ in range(num_courses):
        course = Course("", "", "")  # Create empty course object
        course.input_info()  # Let the user input ID, name, and credits
        school.add_course(course)

def input_marks_for_course(school):
    course_id = input("Enter the course ID to input marks for: ")
    for student in self._students:
        mark = float(input(f"Enter mark for {student._name} in {self._courses[course_id]._name}: "))
        student.add_mark(course_id, mark)