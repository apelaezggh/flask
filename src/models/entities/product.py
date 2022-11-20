class Product():

    def __init__(self, id, name=None, unit_measure=None):
        self.id = id
        self.name = name
        self.unit_measure = unit_measure

    def to_JSON(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'unit_measure' : self.unit_measure,
        }

