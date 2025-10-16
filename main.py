from creature import Creature
from species import Species

creatures = []
species = []

def create_species():
    print('\n\n')
    name = input('Species name: ')
    attr_names = []
    while True:
        attr_name = input("Name of species-specific attribute (or -1 to finish species creation): ")
        if attr_name == '-1': break
        else: attr_names.append(attr_name)

    species.append(Species(attr_names))


def create_creature():
    pass


def view_creature():
    pass

def view_creatures():
    pass


def home():
    print('Creature Creator\n[1] Create a species\n[2] Create a creature\n[3] View current creatures\n[4] Exit')
    choice = input("Your choice: ")
    match choice:
        case '1': print('1')
        case '2': print('2')
        case '3': print('3')
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