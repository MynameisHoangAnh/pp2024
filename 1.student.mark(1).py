


def input_num_students():
    #Inputs and validates the number of students.
    while True:
        num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                return num_students
        else:
            print("Invalid number of students. Please enter a positive integer.")
                
        
def input_student_info():
    #Inputs student information and stores it in a list of tuples.
    students = []
    for i in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        student_info = (student_id, name, dob)
        students.append(student_info)
    return students

def input_num_courses():
    #Inputs and validates the number of courses.
    while True:
        try:
            num_courses = int(input("Enter the number of courses: "))
            if num_courses > 0:
                return num_courses
            else:
                print("Invalid number of courses. Please enter a positive integer.")
        

def input_course_info():
    #Inputs course information and stores it in a dictionary.
    courses = {}
    for i in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses[course_id] = name
    return courses

def input_marks_for_course(students, courses):
    #Inputs marks for a selected course and stores them in a dictionary.
    course_id = input("Enter the course ID to input marks for: ")
    course_marks = {}
    for student in students:
        mark = float(input(f"Enter mark for {student[1]} in {courses[course_id]}: "))
        course_marks[student[0]] = mark
    return course_marks

def list_courses(courses):
    #Lists all available courses.
    print("Available courses:")
    for course_id, name in courses.items():
        print(f"- {course_id}: {name}")

def list_students(students):
    #Lists all students.
    print("Students:")
    for student_id, name, dob in students:
        print(f"- ID: {student_id}, Name: {name}, Date of Birth: {dob}")

def show_student_marks_for_course(course_marks):
    #Shows student marks for a given course.
    print("Student Marks:")
    for student_id, mark in course_marks.items():
        print(f"- {student_id}: {mark}")


# Main program execution
num_students = input_num_students()
students = input_student_info()
num_courses = input_num_courses()
courses = input_course_info()
course_marks = input_marks_for_course(students, courses)

# Call listing functions as needed
list_courses(courses)
list_students(students)
show_student_marks_for_course(course_marks)
