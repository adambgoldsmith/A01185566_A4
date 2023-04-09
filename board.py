"""
Adam Goldsmith
A01185566
"""
import random
from character import *


def create_board(columns: int, rows: int) -> dict:
    """
    Generate game board

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows must be a positive integer that is greater than or equal to 5
    :precondition: columns must be a positive integer that is greater than or equal to 5
    :postcondition: creates a dictionary of board coordinates with a random room assigned to each space.
    :return: the game board as a dictionary.
    """
    events = create_events_list(rows, columns)
    board = {}
    if rows < 5 or columns < 5:
        raise ValueError(f"Board dimensions must be 5 or greater.")
    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0:
                board[(column, row)] = 'start'
            elif row == (rows-1) and column == (columns-1):
                board[(column, row)] = 'boss'
            else:
                event = random.choice(events)
                board[(column, row)] = event
                events.remove(event)
    return board


def create_events_list(rows: int, columns: int) -> list:
    """
    Create list of events

    :param rows: An integer
    :param columns: An integer
    :precondition: rows must be a positive integer greater than or equal to 5
    :precondition: columns must be a positive integer greater than or equal to 5
    :postcondition: creates a list of events
    :return: a list of events
    """
    events = ['chest', 'chest', 'nymph', 'nymph', 'shop', 'shop']
    empty_events = ['empty' for _ in range(rows * columns - 8)]
    events += empty_events
    return events


def display_region(region: list) -> None:
    """
    Display region name

    :param region: A list
    :precondition: region must be a list created by the get_region() function
    :postcondition: prints the region name to the screen

    >>> region_test = ['region_name']
    >>> display_region(region_test)
    -------------------------
    region_name
    """
    print(f"-------------------------")
    print(region[0])


def display_board(rows: int, columns: int, character: dict) -> None:
    """
    Display board

    :param rows: A positive integer
    :param columns: A positive integer
    :param character: A dictionary
    :precondition: rows must be a positive integer greater than or equal to 3
    :precondition: columns must be a positive integer greater than or equal to 3
    :precondition: character must be a dictionary created by the make_character() function
    :postcondition: prints a visual representation of the board to the screen

    >>> character_test = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> display_board(3, 3, character_test)
    o/ [] []
    [] [] []
    [] [] []
    >>> character_test = {'X-coordinate': 1, 'Y-coordinate': 0}
    >>> display_board(2, 2, character_test)
    [] o/
    [] []
    """
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    for row in range(rows):
        for column in range(columns):
            if column != columns - 1:
                final_char = ' '
            else:
                final_char = ''
            if (column, row) == character_location:
                print('o/', end=final_char)
            else:
                print('[]', end=final_char)
        print()


def describe_current_location(region: list) -> None:
    """
    Describe current location

    :param region: A list
    :precondition: region must be a list created by the get_region() function
    :postcondition: prints a description of the current location to the screen
    """
    random_description = random.choice(region[1:5])
    print(random_description)
    print()


def get_user_choice(character: dict) -> str:
    """
    Get direction input
    
    :param character: a dictionary
    :precondition: character must be a dictionary created by the make_character() function
    :postcondition: get the user's desired direction
    :return: the user's desired direction as a string
    """
    options = ['1', '2', '3', '4', 'north', 'south', 'east', 'west']
    while True:
        print(f"Which direction will you travel?\n"
              f"1. north\n2. south\n3. east\n4. west\n0. inventory")
        user_input = input().lower()
        if user_input in options:
            return user_input
        elif user_input == '0':
            check_inventory(character)
        else:
            print(f"That is not a valid direction! Please try again.")


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Validate move

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a string
    :precondition: board must be a dictionary created by make_board() function
    :precondition: character must be a dictionary created by the make_character() function
    :precondition: direction must be a string: '1', 'north', '2', 'south', '3', 'east', '4', 'west'
    :postcondition: verify if the chosen direction is within the bounds of the board
    :return: the validity of the movement as a boolean

    >>> board_test = {(0, 0): 'room', (0, 1): 'room', (1, 0): 'room', (1, 1): 'room'}
    >>> character_test = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> direction_test = 'south'
    >>> validate_move(board_test, character_test, direction_test)
    True
    >>> board_test = {(0, 0): 'room', (0, 1): 'room', (1, 0): 'room', (1, 1): 'room'}
    >>> character_test = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> direction_test = 'north'
    >>> validate_move(board_test, character_test, direction_test)
    False
    """
    new_location = [character['X-coordinate'], character['Y-coordinate']]
    if direction == '1' or direction == 'north':
        new_location[1] -= 1
    elif direction == '2' or direction == 'south':
        new_location[1] += 1
    elif direction == '3' or direction == 'east':
        new_location[0] += 1
    elif direction == '4' or direction == 'west':
        new_location[0] -= 1
    if tuple(new_location) in board:
        return True
    else:
        return False


def move_character(character: dict, direction: str) -> None:
    """
    Move character

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be a dictionary created by the make_character() function
    :precondition: direction must be a string: '1', 'north', '2', 'south', '3', 'east', '4', 'west'
    :postcondition: updates the coordinates of the character

    >>> character_test = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> direction_test = 'south'
    >>> move_character(character_test, direction_test)
    >>> character_test
    {'X-coordinate': 0, 'Y-coordinate': 1}
    >>> character_test = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> direction_test = 'east'
    >>> move_character(character_test, direction_test)
    >>> character_test
    {'X-coordinate': 1, 'Y-coordinate': 0}
    """
    if direction == '1' or direction == 'north':
        character['Y-coordinate'] -= 1
    elif direction == '2' or direction == 'south':
        character['Y-coordinate'] += 1
    elif direction == '3' or direction == 'east':
        character['X-coordinate'] += 1
    elif direction == '4' or direction == 'west':
        character['X-coordinate'] -= 1
