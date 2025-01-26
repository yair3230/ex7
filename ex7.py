import csv

# Global BST root
owner_root = None
MAIN_MENU = """
=== Main Menu ===
1) New Pokedex
2) Existing Pokedex
3) Delete a Pokedex
4) Sort owners
5) Print all
6) Exit"""
STARTER_MENU = '''Choose your starter Pokemon:
1) Treecko
2) Torchic
3) Mudkip'''
POKEDEX_MENU = '''
-- {}'s Pokedex Menu --
1. Add Pokemon
2. Display Pokedex
3. Release Pokemon
4. Evolve Pokemon
5. Back to Main
'''
FILTER_MENU = '''-- Display Filter Menu --
1. Only a certain Type
2. Only Evolvable
3. Only Attack above __
4. Only HP above __
5. Only names starting with letter(s)
6. All of them!
7. Back
'''


########################
# 0) Read from CSV -> HOENN_DATA
########################


def read_hoenn_csv(filename):
    """
    Reads 'hoenn_pokedex.csv' and returns a list of dicts:
      [ { "ID": int, "Name": str, "Type": str, "HP": int,
          "Attack": int, "Can Evolve": "TRUE"/"FALSE" },
        ... ]
    """
    data_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')  # Use comma as the delimiter
        first_row = True
        for row in reader:
            # It's the header row (like ID,Name,Type,HP,Attack,Can Evolve), skip it
            if first_row:
                first_row = False
                continue

            # row => [ID, Name, Type, HP, Attack, Can Evolve]
            if not row or not row[0].strip():
                break  # Empty or invalid row => stop
            d = {
                "ID": int(row[0]),
                "Name": str(row[1]),
                "Type": str(row[2]),
                "HP": int(row[3]),
                "Attack": int(row[4]),
                "Can Evolve": str(row[5]).upper()
            }
            data_list.append(d)
    return data_list


HOENN_DATA = read_hoenn_csv("hoenn_pokedex.csv")


########################
# 1) Helper Functions
########################

def read_int_safe(prompt):
    """
    Prompt the user for an integer, re-prompting on invalid input.
    """
    pass


def get_poke_dict_by_id(poke_id):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by ID, or None if not found.
    """
    pass


def get_poke_dict_by_name(name):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by name, or None if not found.
    """
    pass


def display_pokemon_list(poke_list):
    """
    Display a list of Pokemon dicts, or a message if empty.
    """
    for pokemon in poke_list:
        print(f"ID: {pokemon['ID']}, Name: {pokemon['Name']}, Type: {pokemon['Type']},"
              f" HP: {pokemon['HP']}, Attack: {pokemon['Attack']}, Can Evolve: {pokemon['Can Evolve']}")


########################
# 2) BST (By Owner Name)
########################

def create_owner_node(owner_name, first_pokemon=None):
    """
    Create and return a BST node dict with keys: 'owner', 'pokedex', 'left', 'right'.
    """
    index = first_pokemon - 1
    return {'name': owner_name, 'pokedex': [HOENN_DATA[index]], 'left': None, 'right': None}


def insert_owner_bst(root, new_node):
    """
    Insert a new BST node by owner_name (alphabetically). Return updated root.
    """
    if root is None:
        return new_node
    name = new_node['name']
    name = name.lower()
    current_root = root
    while current_root is not None:
        current_name = current_root['name']
        current_name = current_name.lower()
        if name == current_name:
            print("Name already exists")  # TODO check
            return False
        if name < current_name:
            if current_root['left'] is None:
                current_root['left'] = new_node
                break
            # Else
            current_root = current_root['left']
        elif name > current_name:
            if current_root['right'] is None:
                current_root['right'] = new_node
                break
            # Else
            current_root = current_root['right']
    return root


def find_owner_bst(root, owner_name):
    """
    Locate a BST node by owner_name. Return that node or None if missing.
    owner_name has to be .lower()
    """
    if root is None:
        return None
    if root['name'].lower() == owner_name:
        return root

    attempt_left = find_owner_bst(root['left'], owner_name)
    if attempt_left:
        return attempt_left
    attempt_right = find_owner_bst(root['right'], owner_name)
    if attempt_right:
        return attempt_right
    return None


def min_node(node):
    """
    Return the leftmost node in a BST subtree.
    """
    pass


def delete_owner_bst(root, owner_name):
    """
    Remove a node from the BST by owner_name. Return updated root.
    """
    pass


########################
# 3) BST Traversals
########################

def bfs_traversal(root):
    """
    BFS level-order traversal. Print each owner's name and # of pokemons.
    """
    pass


def pre_order(root):
    """
    Pre-order traversal (root -> left -> right). Print data for each node.
    """
    pass


def in_order(root):
    """
    In-order traversal (left -> root -> right). Print data for each node.
    """
    pass


def post_order(root):
    """
    Post-order traversal (left -> right -> root). Print data for each node.
    """
    pass


########################
# 4) Pokedex Operations
########################

def add_pokemon_to_owner(owner_node):
    """
    Prompt user for a Pokemon ID, find the data, and add to this owner's pokedex if not duplicate.
    """
    valid_choice = False
    poke_id = -1
    while not valid_choice:
        poke_id = input("Enter Pokemon ID to add:")
        if not poke_id.isdecimal():
            print("Invalid choice")  # TODO check this
            continue
        poke_id = int(poke_id)
        if poke_id < 1 or poke_id > 135:
            print("Invalid choice")  # TODO check this
            continue
        valid_choice = True
    # Get all pokemon IDs
    pokemons_ids = [pokemon['ID'] for pokemon in owner_node['pokedex']]
    if poke_id in pokemons_ids:
        print("Pokemon already in the list. No changes made.")
        return
    pokemon_data = HOENN_DATA[poke_id - 1]
    owner_node['pokedex'].append(pokemon_data)
    print(f"Pokemon {pokemon_data['Name']} (ID {pokemon_data['ID']}) added to {owner_node['name']}'s Pokedex.")


def release_pokemon_by_name(owner_node):
    """
    Prompt user for a Pokemon name, remove it from this owner's pokedex if found.
    """
    # Enumarate returns a tuple: (index, pokemon)
    index_to_remove = -1
    pokemon_name = ''
    name = input("Enter Pokemon Name to release:")
    name_lower = name.lower()
    for index, pokemon in enumerate(owner_node['pokedex']):
        pokemon_name = pokemon['Name']
        if pokemon_name.lower() == name_lower:
            index_to_remove = index
            break  # found it, stop searching
    if index_to_remove != -1:
        print(f"Releasing {pokemon_name} from {owner_node['name']}.")
        owner_node['pokedex'].pop(index_to_remove)
    else:
        print(f"No Pokemon named '{name}' in Eliyahu's Pokedex.")


def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, remove it immediately
    """
    name = input('Enter Pokemon Name to evolve:')
    name_lower = name.lower()
    index_to_remove = -1
    pokemon_to_evolve = None
    pokemon_name = ''

    # find pokemon
    for index, pokemon in enumerate(owner_node['pokedex']):
        pokemon_name = pokemon['Name']
        if pokemon_name.lower() == name_lower:
            index_to_remove = index
            pokemon_to_evolve = pokemon
            break  # found it, stop searching

    if index_to_remove == -1:
        print("Pokemon not found")  # TODO check
        return
    if pokemon_to_evolve['Can Evolve'] == 'FALSE':
        print("Pokemon cannot evolve")  # TODO check
        return

    # Else, Find evolution
    evolution_id = pokemon_to_evolve['ID'] + 1
    evolved_pokemon = HOENN_DATA[evolution_id - 1]
    print(f"Pokemon evolved from {pokemon_name} (ID {evolution_id - 1})"
          f" to {evolved_pokemon['Name']} (ID {evolution_id}).")

    # Remove old
    owner_node['pokedex'].pop(index_to_remove)

    if evolved_pokemon in owner_node['pokedex']:
        # Display this message, but nothing left to do
        print('Marshtomp was already present; releasing it immediately.')
    else:
        # Actually add the evolution to the list
        owner_node['pokedex'].append(evolved_pokemon)


########################
# 5) Sorting Owners by # of Pokemon
########################

def gather_all_owners(root, arr):
    """
    Collect all BST nodes into a list (arr).
    """
    pass


def sort_owners_by_num_pokemon():
    """
    Gather owners, sort them by (#pokedex size, then alpha), print results.
    """
    pass


########################
# 6) Print All
########################

def print_all_owners():
    """
    Let user pick BFS, Pre, In, or Post. Print each owner's data/pokedex accordingly.
    """
    pass


def pre_order_print(node):
    """
    Helper to print data in pre-order.
    """
    pass


def in_order_print(node):
    """
    Helper to print data in in-order.
    """
    pass


def post_order_print(node):
    """
    Helper to print data in post-order.
    """
    pass


########################
# 7) The Display Filter Sub-Menu
########################

def display_filter_sub_menu(owner_node):
    """
    1) Only type X
    2) Only evolvable
    3) Only Attack above
    4) Only HP above
    5) Only name starts with
    6) All
    7) Back
    """
    print(FILTER_MENU)
    choice = -1
    while choice != '7':
        choice = input("Your choice:")
        pokemon_list = []
        if choice == '1':
            lower_type = input("Which Type? (e.g. GRASS, WATER):")
            lower_type = lower_type.lower()

            for pokemon in owner_node['pokedex']:
                if pokemon['Type'].lower() == lower_type:
                    pokemon_list.append(pokemon)

            # In one line:
            # pokemon_list = [pokemon for pokemon in owner_node['pokedex'] if pokemon['Type'].lower() == lower_type]
        elif choice == '2':
            # Note that for some dumb reason "can evolve" is a string and not a bool
            pokemon_list = [pokemon for pokemon in owner_node['pokedex'] if pokemon['Can Evolve'] == 'TRUE']
        elif choice == '3':
            attack_threshold = input("Enter Attack threshold:")
            if not attack_threshold.isdecimal():
                print("Invalid input")  # TODO check
                continue
            attack_threshold = int(attack_threshold)
            for pokemon in owner_node['pokedex']:
                if pokemon['Attack'] > attack_threshold:
                    pokemon_list.append(pokemon)

            # In one line:
            # pokemon_list = [pokemon for pokemon in owner_node['pokedex'] if pokemon['Attack'] > attack_threshold]
        elif choice == '4':
            hp_threshold = input("Enter HP threshold:")
            if not hp_threshold.isdecimal():
                print("Invalid input")  # TODO check
                continue
            hp_threshold = int(hp_threshold)
            for pokemon in owner_node['pokedex']:
                if pokemon['HP'] > hp_threshold:
                    pokemon_list.append(pokemon)
            # In one line:
            # pokemon_list = [pokemon for pokemon in owner_node['pokedex'] if pokemon['HP'] > hp_threshold]
        elif choice == '5':
            letters = input("Starting letter(s):")
            lower_letters = letters.lower()
            for pokemon in owner_node['pokedex']:
                name_lower = pokemon['Name'].lower()
                if name_lower.startswith(lower_letters):
                    pokemon_list.append(pokemon)
            # In one line:
            # pokemon_list = [pokemon for pokemon in owner_node['pokedex']
            #                 if pokemon['Name'].lower().startswith(lower_letters)]
        elif choice == '6':
            pokemon_list = [pokemon for pokemon in owner_node['pokedex']]
        elif choice == '7':
            break
        if pokemon_list:
            display_pokemon_list(pokemon_list)
        else:
            print('There are no Pokemons in this Pokedex that match the criteria.')


########################
# 8) Sub-menu & Main menu
########################

def create_pokedex(owner_root):
    name = input("Owner name:")
    print(STARTER_MENU)
    if find_owner_bst(owner_root, name.lower()):
        print(f"Owner '{name}' already exists. No new Pokedex created.")
        return

    starter_choice = input("Your choice:")
    while starter_choice not in ['1', '2', '3']:
        print("Invalid input")  # TODO check
        starter_choice = input("Your choice:")
    starter_choice = int(starter_choice)
    # Convert input to index and multiply by 3 to find the correct starter
    starter_choice = (starter_choice - 1) * 3

    new_node = create_owner_node(name, starter_choice + 1)  # Convert from index back to id
    owner_root = insert_owner_bst(owner_root, new_node)

    starter_name = new_node['pokedex'][0]['Name']
    print('New Pokedex created for {} with starter {}.'.format(new_node['name'], starter_name))
    return owner_root


def existing_pokedex():
    """
    Ask user for an owner name, locate the BST node, then show sub-menu:
    - Add Pokemon
    - Display (Filter)
    - Release
    - Evolve
    - Back
    """
    global owner_root
    name = input("Owner name:")
    lower_name = name.lower()
    node = find_owner_bst(owner_root, name)
    if not node:
        print(f"Owner '{name}' not found.")
        return
    # Else

    choice = -1
    while choice != '5':
        print(POKEDEX_MENU.format(name))
        choice = input("Your choice:")
        if choice == '1':
            add_pokemon_to_owner(node)
        elif choice == '2':
            display_filter_sub_menu(node)
        elif choice == '3':
            release_pokemon_by_name(node)
        elif choice == '4':
            evolve_pokemon_by_name(node)
        elif choice == '5':
            pass
        else:
            print('Invalid choice')  # TODO check this


def main_menu():
    """
    Main menu for:
    1) New Pokedex
    2) Existing Pokedex
    3) Delete a Pokedex
    4) Sort owners
    5) Print all
    6) Exit
    """
    global owner_root
    choice = -1
    while choice != '6':
        print(MAIN_MENU)
        choice = input("Your choice:")

        # Ensure choice is digit
        if not choice.isdigit():
            print("Invalid input")  # TODO check
        elif choice == '1':
            owner_root = create_pokedex(owner_root)
        elif choice == '2':
            existing_pokedex()
        else:
            print("Invalid input")  # TODO check


def main():
    """
    Entry point: calls main_menu().
    """
    main_menu()


if __name__ == "__main__":
    main()
