import csv

# Global BST root
owner_root = None
MAIN_MENU = """
=== Main Menu ===
1. New Pokedex
2. Existing Pokedex
3. Delete a Pokedex
4. Display owners by number of Pokemon
5. Print All
6. Exit"""
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
PRINT_OWNERS_MENU = '''1) BFS
2) Pre-Order
3) In-Order
4) Post-Order
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
    return {'name': owner_name,
            'pokedex': [HOENN_DATA[index]],
            'left': None, 'right': None}


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
            print(f"Owner '{new_node['name']}' already exists. No new Pokedex created.")
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
    while node['left'] is not None:
        node = node['left']
    return node


def delete_owner_bst(root, owner_name):
    if not root:
        return root

    # Find the node to remove
    if owner_name < root['name']:
        root['left'] = delete_owner_bst(root['left'], owner_name)
    elif owner_name > root['name']:
        root['right'] = delete_owner_bst(root['right'], owner_name)
    else:
        # Node to be removed found
        # Case 1: Node with no children (leaf node)
        if not root['left'] and not root['right']:
            return None

        # Case 2: Node with one child
        if not root['left']:
            return root['right']
        elif not root['right']:
            return root['left']

        # Case 3: Node with two children
        # Find the in-order successor (smallest value in the right subtree)
        successor = min_node(root['right'])
        root['name'] = successor['name']
        root['pokedex'] = successor['pokedex']
        root['right'] = delete_owner_bst(root['right'], successor['name'])

    return root


def delete_owner(root):
    name = input('Enter owner to delete: ')
    if find_owner_bst(root, name):
        print(f"Deleting {name}'s entire Pokedex...")
        root = delete_owner_bst(root, name)
        print(f'Pokedex deleted.')
        return root
    else:
        print(f"Owner '{name}' not found.")
        return root


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
        poke_id = input("Enter Pokemon ID to add: ")
        if not poke_id.isdecimal():
            print(f"ID {poke_id} not found in Honen data.")
            return
        poke_id = int(poke_id)
        if poke_id < 1 or poke_id > 135:
            print(f"ID {poke_id} not found in Honen data.")
            return
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
    # Enumerate returns a tuple: (index, pokemon)
    index_to_remove = -1
    pokemon_name = ''
    name = input("Enter Pokemon Name to release: ")
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
        print(f"No Pokemon named '{name}' in {owner_node['name']}'s Pokedex.")


def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, remove it immediately
    """
    name = input('Enter Pokemon Name to evolve: ')
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
        print(f"No Pokemon named '{name}' in {owner_node['name']}'s Pokedex.")
        return
    if pokemon_to_evolve['Can Evolve'] == 'FALSE':
        print(f"{name} cannot evolve.")
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
def gather_all_owners_inner(root, arr):
    arr.append(root)
    if root['left']:
        arr = gather_all_owners_inner(root['left'], arr)
    if root['right']:
        arr = gather_all_owners_inner(root['right'], arr)
    return arr


def gather_all_owners(root):
    """
    Collect all BST nodes into a list (arr).
    """
    return gather_all_owners_inner(root, [])


def sort_owners_by_num_pokemon(root):
    """
    Gather owners, sort them by (#pokedex size, then alpha), print results.
    """
    owners_arr: list = gather_all_owners(root)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for index in range(len(owners_arr) - 1):
            current_len = len(owners_arr[index]['pokedex'])
            next_len = len(owners_arr[index + 1]['pokedex'])
            if current_len == next_len:
                current_name = owners_arr[index]['name']
                next_name = owners_arr[index + 1]['name']
                if current_name > next_name:
                    # "Swap"
                    temp = owners_arr.pop(index + 1)
                    owners_arr.insert(index, temp)
                    is_sorted = False
            elif current_len > next_len:
                # "Swap"
                temp = owners_arr.pop(index + 1)
                owners_arr.insert(index, temp)
                is_sorted = False

    print('=== The Owners we have, sorted by number of Pokemons ===')
    for owner in owners_arr:
        print(f"Owner: {owner['name']} (has {len(owner['pokedex'])} Pokemon)")


########################
# 6) Print All
########################
def print_owner(owner):
    print()
    print(f'Owner: {owner["name"]}')
    display_pokemon_list(owner["pokedex"])


def print_all_owners(root):
    """
    Let user pick BFS, Pre, In, or Post. Print each owner's data/pokedex accordingly.
    """

    print(PRINT_OWNERS_MENU)
    choice = input("Your choice: ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        choice = input("Your choice: ")
    if choice == '1':
        bfs_print(root)
    elif choice == '2':
        pre_order_print(root)
    elif choice == '3':
        in_order_print(root)
    elif choice == '4':
        post_order_print(root)


def bfs_print(node):
    """
    Helper to print data in pre-order.
    """
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        print_owner(current_node)
        if current_node["left"]:
            queue.append(current_node["left"])
        if current_node["right"]:
            queue.append(current_node["right"])


def pre_order_print(node):
    """
    Helper to print data in pre-order.
    """
    print_owner(node)
    if node["left"]:
        pre_order_print(node["left"])
    if node["right"]:
        pre_order_print(node["right"])


def in_order_print(node):
    """
    Helper to print data in in-order.
    """
    if node["left"]:
        in_order_print(node["left"])
    print_owner(node)
    if node["right"]:
        in_order_print(node["right"])


def post_order_print(node):
    """
    Helper to print data in post-order.
    """
    if node["left"]:
        post_order_print(node["left"])
    if node["right"]:
        post_order_print(node["right"])
    print_owner(node)


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
    choice = -1
    while choice != '7':
        print(FILTER_MENU)
        choice = input("Your choice: ")
        pokemon_list = []
        if choice == '1':
            lower_type = input("Which Type? (e.g. GRASS, WATER): ")
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

            while True:
                attack_threshold = input("Enter Attack threshold: ")
                if attack_threshold.isdecimal():
                    break
                if len(attack_threshold) == 0:
                    print("Invalid input.")
                # either not a number, or a negative number. we allow negative numbers
                if attack_threshold[0] == '-':
                    attack_threshold = attack_threshold[1:]
                    if attack_threshold.isdecimal():
                        attack_threshold = 0
                        break
                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")

            attack_threshold = int(attack_threshold)
            for pokemon in owner_node['pokedex']:
                if pokemon['Attack'] > attack_threshold:
                    pokemon_list.append(pokemon)

            # In one line:
            # pokemon_list = [pokemon for pokemon in owner_node['pokedex'] if pokemon['Attack'] > attack_threshold]
        elif choice == '4':
            while True:
                hp_threshold = input("Enter HP threshold: ")
                if hp_threshold.isdecimal():
                    break
                if len(hp_threshold) == 0:
                    print("Invalid input.")
                # either not a number, or a negative number. we allow negative numbers
                if hp_threshold[0] == '-':
                    hp_threshold = hp_threshold[1:]
                    if hp_threshold.isdecimal():
                        hp_threshold = 0
                        break
                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")

            hp_threshold = int(hp_threshold)
            for pokemon in owner_node['pokedex']:
                if pokemon['HP'] > hp_threshold:
                    pokemon_list.append(pokemon)
            # In one line:
            # pokemon_list = [pokemon for pokemon in owner_node['pokedex'] if pokemon['HP'] > hp_threshold]
        elif choice == '5':
            letters = input("Starting letter(s): ")
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
    name = input("Owner name: ")
    print(STARTER_MENU)
    if find_owner_bst(owner_root, name.lower()):
        print(f"Owner '{name}' already exists. No new Pokedex created.")
        return

    starter_choice = input("Your choice: ")
    while starter_choice not in ['1', '2', '3']:
        print("Invalid input.")
        starter_choice = input("Your choice: ")
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
    name = input("Owner name: ")
    lower_name = name.lower()
    node = find_owner_bst(owner_root, lower_name)
    if not node:
        print(f"Owner '{name}' not found.")
        return
    # Else

    choice = -1
    while choice != '5':
        print(POKEDEX_MENU.format(node['name']))
        choice = input("Your choice: ")
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
            print('Invalid choice')


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
        choice = input("Your choice: ")

        # Ensure choice is digit
        if not choice.isdigit():
            print("Invalid choice.")
        elif choice == '1':
            owner_root = create_pokedex(owner_root)
        elif choice == '2':
            if owner_root is None:
                print('No owners at all.')
                continue
            existing_pokedex()
        elif choice == '3':
            owner_root = delete_owner(owner_root)
        elif choice == '4':
            sort_owners_by_num_pokemon(owner_root)
        elif choice == '5':
            print_all_owners(owner_root)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

    print("Goodbye!")


def main():
    """
    Entry point: calls main_menu().
    """
    main_menu()


if __name__ == "__main__":
    main()
