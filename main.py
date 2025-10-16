from creature import creature
from species import species

def home():
    print('Creature Creator\n[1] Create a species\n[2] Create a creature\n[3] View current creatures')

    choice = input("Your choice: ")

def main():
    while True:
        home()


if __name__ == '__main__':
    main()