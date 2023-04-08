from character import *

def shop(character: dict) -> None:
    """
    Start shop event

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Commence the shop event
    """
    print(f"-------------------------f")
    print(f"You notice a small trade sfhip gliding through the air. The large wooden propeller on its roof clicks loudly with each rotation.\n"
          f"You float up next to the shfip, dock, and climb aboard.\n"
          f"A grubby, short, hobgoblin sfhop keeper welcomes you in...")
    user_shop_choice(character)

def user_shop_choice(character: dict) -> None:
    """
    Get user shop choice

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Get user shop choice
    """
    while True:
        user_choice = input(f"\"Hello friend! Interested in my wares?\"\n"
                            f"1. Buy 2 flux (10 gold)\n"
                            f"2. Buy repair kit (30 gold)\n"
                            f"3. Leave shop\n"
                            f"0. Inventory\n")
        if user_choice == '1' or user_choice == '2':
            sufficient_gold(user_choice, character)
        elif user_choice == '3':
            print(f"Goodbye, friend!\n")
            break
        elif user_choice == '0':
            check_inventory(character)
        else:
            print(f"I don't know what you mean, friend. Please try again.\n")

def sufficient_gold(user_input: str, character: dict) -> None:
    """
    Check gold amount

    :param user_input: A string
    :param character: A dictionary
    :precondition: user_input must be a string
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Check if user has enough gold to buy an item
    """
    if user_input == '1':
        if character['inventory']['gold'] >= 10:
            buy_flux(character)
        else:
            print(f"You don't have enough gold, friend.\n")
    elif user_input == '2':
        if character['inventory']['gold'] >= 30:
            buy_repair_kit(character)
        else:
            print(f"You don't have enough gold, friend.\n")

def buy_flux(character: dict) -> None:
    """
    Buy flux

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Buy flux and reduce gold
    """
    character['inventory']['flux'] += 2
    character['inventory']['gold'] -= 10
    print(f"You bought 2 flux for 10 gold.\n")

def buy_repair_kit(character: dict) -> None:
    """
    Buy repair kit

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Buy repair kit and reduce gold
    """
    character['inventory']['repair_kits'] += 1
    character['inventory']['gold'] -= 30
    print(f"You bought a repair kit for 30 gold.\n")