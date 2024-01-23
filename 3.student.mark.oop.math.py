import math
import numpy as np
import curses

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
        # Round down mark to 1-digit decimal using math.floor()
        self._marks[course_id] = math.floor(mark * 10) / 10


class Course:
    def __init__(self, id, name, credits):
        self._id = id
        self._name = name
        self._credits = credits #Store course credits

    def input_info(self):
        self._id = input("Enter course ID: ")
        self._name = input("Enter course name: ")

    def input_info(self):
        self._id = input("Enter course ID: ")
        self._name = input("Enter course name: ")
        self._credits = int(input("Enter course credits: "))  # Collect credits

    def get_credits(self):
        return self._credits

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
            course = Course("", "", "")  # Create empty course object
            course.input_info()  # Let the user input ID, name, and credits
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
    
    def get_student_by_id(self, student_id):
        for student in self._students:
            if student._id == student_id:
                return student
        return None  # Return None if student not found

    
    def calculate_gpa(self, student_id):
        student = self.get_student_by_id(student_id)
        if not student:
            return 0

        total_credits = 0
        weighted_sum = 0
        for course_id, mark in student._marks.items():
            course = self._courses[course_id]
            credits = course.get_credits()  # Assuming you've added a get_credits() method to Course
            total_credits += credits
            weighted_sum += mark * credits

        return weighted_sum / total_credits if total_credits > 0 else 0

    def sort_students_by_gpa(self):
        self._students.sort(key=lambda student: self.calculate_gpa(student._id), reverse=True)
    def display_ui(self):
        stdscr = curses.initscr()  # Initialize curses screen
        curses.noecho()
        curses.cbreak()

        while True:
            stdscr.clear()  # Clear the screen
            stdscr.addstr(0, 0, "School Management System")
            stdscr.addstr(2, 0, "1. List students")
            stdscr.addstr(3, 0, "2. List courses")
            stdscr.addstr(4, 0, "3. View student marks")
            stdscr.addstr(5, 0, "4. Exit")
            stdscr.refresh()

            choice = stdscr.getch()  # Get user input
            if choice == ord('1'):
                self.list_students()  # Implement UI for listing students
            elif choice == ord('2'):
                self.list_courses()  # Implement UI for listing courses
            elif choice == ord('3'):
                self.list_marks()
                # Implement UI for viewing student marks (see previous explanations)
            else:
                
                break  # Exit the loop

        curses.endwin()  # Restore terminal settings    
# Main program
school = School()
school.input_students()
school.input_courses()
school.input_marks_for_course()
school.sort_students_by_gpa()
school.display_ui()