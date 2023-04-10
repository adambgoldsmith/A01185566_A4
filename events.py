"""
Adam Goldsmith
A01185566
"""
from chest import *
from shop import *
from boss import *
from nymph import *


def all_events(board: dict, character: dict, region: list) -> None:
    """
    Create event dictionary

    :param board: A dictionary
    :param character: A dictionary
    :param region: A list
    :precondition: Board must be a dictionary created by the create_board() function
    :preconditon: Character must be a dictionary created by the create_character() function
    :precondition: Region must be a list created by the get_region() function
    :postcondition: start an event of a certain event type
    """
    if type(board) is not dict:
        raise TypeError("Board must be a dictionary")
    if type(character) is not dict and len(character) < 10:
        raise TypeError("Character must be a dictionary with correct key/value pairs")
    if type(region) is not list and len(region) < 5:
        raise TypeError("Region must be a list with correct items")
    events = {
        'chest': chest,
        'nymph': nymph,
        'enemy': battle,
        'shop': shop,
        'boss': boss_battle,
    }
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    if board[character_location] == 'chest' or board[character_location] == 'nymph':
        events[board[character_location]](character)
        board[character_location] = 'empty'
    elif board[character_location] == 'shop':
        events['shop'](character)
    elif board[character_location] == 'boss':
        events['boss'](character, region)
    elif board[character_location] == 'empty' or board[character_location] == 'start':
        if random.randint(1, 4) == 1:
            events['enemy'](character)
    else:
        raise ValueError("Board tile does not exist.")
    