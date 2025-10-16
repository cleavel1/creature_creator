from species import species

class creature:
    def __init__(self, name: str, age: int, species: species):
        self.name = name
        self.age = age
        self.species = species

    def get_name(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        return self.age
    
    def get_species(self) -> species:
        return self.species

