class Student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob
        self._marks = {}  # Store marks for each course

    def input_info(self):
        self._id = input("Enter student ID: ")
        self._name = input("Enter student name: ")
        self._dob = input("Enter student date of birth (YYYY-MM-DD): ")

    def list_info(self):
        print(f"ID: {self._id}, Name: {self._name}, Date of Birth: {self._dob}")

    def get_marks(self, course_id):
        return self._marks.get(course_id)

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

class Course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def input_info(self):
        self._id = input("Enter course ID: ")
        self._name = input("Enter course name: ")

    def list_info(self):
        print(f"{self._id}: {self._name}")

class School:
    def __init__(self):
        self._students = []
        self._courses = {}

    def add_student(self, student):
        self._students.append(student)

    def add_course(self, course):
        self._courses[course._id] = course

    def input_students(self):
        num_students = int(input("Input number of students: "))
        for _ in range(num_students):
            student = Student("", "", "")  # Create empty student object
            student.input_info()
            self.add_student(student)

    def input_courses(self):
        num_courses = int(input("Input number of courses: "))
        for _ in range(num_courses):
            course = Course("", "")  # Create empty course object
            course.input_info()
            self.add_course(course)

    def input_marks_for_course(self):
        course_id = input("Enter the course ID to input marks for: ")
        for student in self._students:
            mark = float(input(f"Enter mark for {student._name} in {self._courses[course_id]._name}: "))
            student.add_mark(course_id, mark)

    def list_students(self):
        print("Available student/students:")
        for student in self._students:
            student.list_info()

    def list_courses(self):
        print("Available course/courses:")
        for course in self._courses.values():
            course.list_info()

    def show_student_marks(self, course_id):
        print("Students' marks for course:")
        for student in self._students:
            mark = student.get_marks(course_id)
            if mark:
                print(f"- {student._id}: {mark}")

# Main program
school = School()
school.input_students()
school.input_courses()
school.input_marks_for_course()
school.list_students()
school.list_courses()
school.show_student_marks(input("Enter the course ID to display marks for: "))
