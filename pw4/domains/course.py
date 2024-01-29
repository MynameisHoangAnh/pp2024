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