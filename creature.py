from species import Species

class Creature:
    def __init__(self, name: str, age: int, species: Species):
        self.name = name
        self.age = age
        self.species = species
        self.attributes = []
        for attr in species.attribute_names:
            self.attributes.append({
                'name': attr,
                'value': 'N/A'
            })

    def set_attribute(self, name: str, value: str):
        for attr in self.attributes:
            if attr['name'] == name:
                attr['value'] = value
