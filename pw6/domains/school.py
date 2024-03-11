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

        curses.endwin()  # Restore terminal setting