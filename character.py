def create_character() -> dict:
    """
    Create character

    :return: A dictionary representing the character
    """
    character = {
        'X-coordinate': 0,
        'Y-coordinate': 0,
        'name': 'Captain Magnus Selwood',  # unused, but interesting lore
        'level': 1,
        'experience': 0,
        'max_health': 100,
        'health': 100,
        'attack_power': 10,
        'ability_power': 20,
        'inventory': {
                'flux': 10,
                'repair_kits': 1,
                'gold': 0,
        },
    }
    return character


def is_alive(character: dict) -> bool:
    """
    Check if alive

    :param character: a dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: verify if character is alive
    :return: verification if character is alive as a boolean

    >>> character_test = {'health': 50}
    >>> is_alive(character_test)
    True
    >>> character_test = {'health': 0}
    >>> is_alive(character_test)
    False
    """
    if character['health'] > 0:
        return True
    else:
        return False


def check_inventory(character: dict) -> None:
    """
    Check inventory

    :param character: a dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: display character's inventory
    """
    print(f"Flux: {character['inventory']['flux']}\n"
          f"Repair Kits: {character['inventory']['repair_kits']}\n"
          f"Gold: {character['inventory']['gold']}\n")


def level_up(character: dict) -> None:
    """
    Level up

    :param character: a dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: level up character
    """
    if character['experience'] >= 100:
        character['level'] += 1
        experience_storage = character['experience'] - 100
        character['experience'] = experience_storage
        character['max_health'] += 20
        character['health'] = character['max_health']
        character['attack_power'] += 5
        character['ability_power'] += 5
        print(f"You have leveled up! Your ship's cannons are now stronger and your hull has been reinforced!\n"
              f"You are now level {character['level']}! Your max health is now {character['max_health']} and "
              f"your attack power is now {character['attack_power']}.\n"
              f"Your health has been restored to {character['health']}.\n")


def display_stats(character: dict) -> None:
    """
    Display stats

    :param character: a dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: display character's stats

    >>> character_test = {'health': 100, 'max_health': 100, 'experience': 50, 'level': 1}
    >>> display_stats(character_test)
    HP: 100/100 |~| XP: 50/100 |~| Lvl: 1
    <BLANKLINE>
    """
    print(f"HP: {character['health']}/{character['max_health']} |~|"
          f" XP: {character['experience']}/100 |~|"
          f" Lvl: {character['level']}\n")


def check_if_achieved_goal(board: dict, character: dict) -> bool:
    """
    Check if goal achieved

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary created by make_board() function
    :precondition: character must be a dictionary created by the make_character() function
    :postcondition: verify if player has reached the goal
    :return: verification if player has reached the goal as a boolean

    >>> board_test = {(0, 0): 'empty', (0, 1): 'empty', (1, 0): 'empty', (1, 1): 'empty'}
    >>> character_test = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> check_if_achieved_goal(board_test, character_test)
    False
    >>> board_test = {(0, 0): 'empty', (0, 1): 'empty', (1, 0): 'empty', (1, 1): 'empty'}
    >>> character_test = {'X-coordinate': 1, 'Y-coordinate': 1}
    >>> check_if_achieved_goal(board_test, character_test)
    True
    """
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    if character_location == list(board.keys())[-1]:
        character['X-coordinate'] = 0
        character['Y-coordinate'] = 0
        return True
    else:
        return False
