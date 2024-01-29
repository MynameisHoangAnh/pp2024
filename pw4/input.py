import domains.student as student
import domains.course as course

def input_students(school):
    num_students = int(input("Input number of students: "))
    for _ in range(num_students):
        student = Student("", "", "")  # Create empty student object
        student.input_info()
        self.add_student(student)

def input_courses(school):
    num_courses = int(input("Input number of courses: "))
    for _ in range(num_courses):
        course = Course("", "", "")  # Create empty course object
        course.input_info()  # Let the user input ID, name, and credits
        self.add_course(course)

def input_marks_for_course(school):
    course_id = input("Enter the course ID to input marks for: ")
    for student in self._students:
        mark = float(input(f"Enter mark for {student._name} in {self._courses[course_id]._name}: "))
        student.add_mark(course_id, mark)