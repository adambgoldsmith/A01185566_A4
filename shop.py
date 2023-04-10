"""
Adam Goldsmith
A01185566
"""
from character import *


def shop(character: dict) -> None:
    """
    Start shop event

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Commence the shop event
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary")
    print(f"-------------------------")
    print(f"You notice a small trade ship gliding through the air. "
          f"The large wooden propeller on its roof clicks loudly with each rotation.\n"
          f"You float up next to the ship, dock, and climb aboard.\n"
          f"A grubby, short, hobgoblin shop keeper welcomes you in...")
    user_shop_choice(character)


def user_shop_choice(character: dict) -> None:
    """
    Get user shop choice

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Get user shop choice
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary")
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

    >>> user_input_test = '1'
    >>> character_test = {'inventory': {'gold': 0}}
    >>> sufficient_gold(user_input_test, character_test)
    You don't have enough gold, friend.
    <BLANKLINE>
    """
    if type(user_input) is not str:
        raise TypeError("User_input must be a string")
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary")
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

    >>> character_test = {'inventory': {'gold': 10, 'flux': 0}}
    >>> buy_flux(character_test)
    You bought 2 flux for 10 gold.
    <BLANKLINE>
    >>> character_test
    {'inventory': {'gold': 0, 'flux': 2}}
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary")
    character['inventory']['flux'] += 2
    character['inventory']['gold'] -= 10
    print(f"You bought 2 flux for 10 gold.\n")


def buy_repair_kit(character: dict) -> None:
    """
    Buy repair kit

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Buy repair kit and reduce gold

    >>> character_test = {'inventory': {'gold': 30, 'repair_kits': 0}}
    >>> buy_repair_kit(character_test)
    You bought a repair kit for 30 gold.
    <BLANKLINE>
    >>> character_test
    {'inventory': {'gold': 0, 'repair_kits': 1}}
    """
    if type(character) is not dict:
        raise TypeError("Character must be a dictionary")
    character['inventory']['repair_kits'] += 1
    character['inventory']['gold'] -= 30
    print(f"You bought a repair kit for 30 gold.\n")
