from domains.base import Entity

class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self._dob = dob
        self._marks = {} # Store marks for each course

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
    def to_string(self):
        return f"{self._id},{self._name},{self._dob},{','.join(f'{course_id}:{mark}' for course_id, mark in self._marks.items())}"`

