from creature import Creature
from species import Species

creatures = []
species = []

def create_species(name: str) -> Species:
    print(f'\n{name} Species Creation')
    while name == '' or name == None: name = input('Species name: ')
    attr_names = []
    while True:
        attr_name = input("Name of species-specific attribute (or -1 to finish species creation): ")
        if attr_name == '-1': break
        else: attr_names.append(attr_name)

    new_species = Species(name, attr_names)
    species.append(new_species)
    return new_species


def create_creature():
    print('\n')
    name = input('Creature name: ')
    age = input('Creature age: ')
    species_name = input('Species name: ')
    chosen_species = None
    for sp in species:
        if sp.name == name:
            chosen_species = sp
            break

    if chosen_species == None: 
        chosen_species = create_species(species_name)
        print()

    creature = Creature(name, int(age), chosen_species)

    for attr in creature.attributes:
        attr['value'] = input(f'{name} {attr['name']}: ')

    creatures.append(creature)

    print('Creature created successfuly!')

def view_creature(creature_name: str):
    print()
    for creature in creatures:
        if creature.name == creature_name:
            print(creature.name)
            print(f' Species: {creature.species.name}')
            print(f' Age: {creature.age}')
            print(f' {creature.species.name} specific attributes:')
            for attribute in creature.attributes:
                print(f'  {attribute['name']}: {attribute['value']}')

def view_creatures():
    for creature in creatures:
        print(f'{creature.name}: {creature.species.name}, Age: {creature.age}')

    view_specific = input('view a specific creature (y/n)? ')
    if view_specific == 'y' or view_specific == 'yes':
        name = input("name: ")
        view_creature(name)

def home():
    print('\nCreature Creator\n[1] Create a species\n[2] Create a creature\n[3] View current creatures\n[4] Exit')
    choice = input("Your choice: ")
    match choice:
        case '1': create_species('')
        case '2': create_creature()
        case '3': view_creatures()
        case '4': 
            print('Exiting...')
            exit(0)
        case _: 
            print('Error: invalid input')
            home()

def main():
    while True:
        home()


if __name__ == '__main__':
    main()