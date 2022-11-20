class User():

    def __init__(self, id, name=None, password=None, cell=None):
        self.id = id
        self.name = name
        self.password = password
        self.cell = cell

    def to_JSON(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'password' : self.password,
            'cell' : self.cell
        }

