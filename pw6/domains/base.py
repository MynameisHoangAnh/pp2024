class Entity:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def to_string(self):
        # Implement data serialization for writing
        raise NotImplementedError
