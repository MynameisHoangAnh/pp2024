from domains.base import Entity

class Course(Entity):
    def __init__(self, id, name, credits):
        super().__init__(id, name)
        self._credits = credits
    def input_info(self):
        self._id = input("Enter course ID: ")
        self._name = input("Enter course name: ")

    def input_info(self):
        self._id = input("Enter course ID: ")
        self._name = input("Enter course name: ")
        self._credits = int(input("Enter course credits: "))  # Collect credits

    def get_credits(self):
        return self._credits
    
    def to_string(self):
        return f"{self._id},{self._name},{self._credits}"