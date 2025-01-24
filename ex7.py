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
    pass


########################
# 2) BST (By Owner Name)
########################

def create_owner_node(owner_name, first_pokemon=None):
    """
    Create and return a BST node dict with keys: 'owner', 'pokedex', 'left', 'right'.
    """
    index = first_pokemon - 1
    print(HOENN_DATA[index])
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
            current_root = current_root['left']
        elif name > current_name:
            current_root = current_root['right']
    current_root = new_node
    return root


def find_owner_bst(root, owner_name):
    """
    Locate a BST node by owner_name. Return that node or None if missing.
    """
    pass


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
    pass


def release_pokemon_by_name(owner_node):
    """
    Prompt user for a Pokemon name, remove it from this owner's pokedex if found.
    """
    pass


def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, remove it immediately
    """
    pass


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
    pass


########################
# 8) Sub-menu & Main menu
########################

def existing_pokedex():
    """
    Ask user for an owner name, locate the BST node, then show sub-menu:
    - Add Pokemon
    - Display (Filter)
    - Release
    - Evolve
    - Back
    """
    name = input("Owner name:")
    lower_name = name.lower()


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
    while choice != 6:
        print(MAIN_MENU)
        choice = input("Your choice:")

        # Ensure choice is digit
        if not choice.isdigit():
            print("Invalid input")  # TODO check
        if choice == '1':
            name = input("Owner name:")
            print(STARTER_MENU)
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


def main():
    """
    Entry point: calls main_menu().
    """
    main_menu()


if __name__ == "__main__":
    main()
