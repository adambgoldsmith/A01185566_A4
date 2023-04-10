"""
Adam Goldsmith
A01185566
"""
import itertools
import random
from helper_functions.character import is_alive
from helper_functions.character import check_inventory


def battle(character: dict) -> None:
    """
    Start battle event

    :param character: A dictionary
    :precondition: Character must be a dictionary created by the create_character() function
    :postcondition: Commence an enemy battle sequence
    """
    if type(character) is not dict:
        raise TypeError("Arguments must be correct data types")
    print(f"-------------------------")
    print(f"You spot a hostile air ship on the horizon. As the ship gets closer,"
          f" your eyes are drawn to the large skull\n"
          f"and crossbones crudely painted on it's side. Pirates! You ready your cannons for battle.")
    enemy = generate_enemy_ship()
    print(f"The enemy ship has {enemy['health']} health and {enemy['attack_power']} attack power.")
    battle_loop(character, enemy)
    if enemy['health'] <= 0:
        character['inventory']['gold'] += 50
        character['experience'] += 25
        print(f"The hostile ship plummets through the clouds and explodes in a fiery ball of flames."
              f" Well done, captain! You stand victorious!\n"
              f"You gain 50 gold coins for your victory.\n"
              f"You gain 25 experience points for your victory.")


def battle_loop(character: dict, enemy: dict) -> None:
    """
    Start battle loop

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Start a new battle loop
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    turns = itertools.cycle([character, enemy])
    while enemy['health'] > 0 and is_alive(character):
        current_turn = next(turns)
        if current_turn == character:
            retreated = user_battle_selection(character, enemy)
            if retreated:
                break
        elif current_turn == enemy:
            enemy_attack(character, enemy)
            if not is_alive(character):
                break


def generate_enemy_ship() -> dict:
    """
    Generate enemy ship

    :return: A dictionary representing an enemy ship
    >>> generate_enemy_ship()
    {'type': 'regular', 'name': 'the pirate ship', 'health': 50, 'attack_power': 10}
    """
    enemy_ship = {
        'type': 'regular',
        'name': 'the pirate ship',
        'health': 50, 
        'attack_power': 10,
    }
    return enemy_ship


def get_user_battle_choice(enemy: dict) -> str:
    """
    Get user battle choice

    :param enemy: A dictionary
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Get the users battle choice
    :return: The users choice as a string
    """
    if type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    while True:
        user_choice = input(f'What is your next move, captain?\n'
                            f'1. Fire cannons\n'
                            f'2. Repair ship (-1 repair kit)\n'
                            f'3. Air Barrage (-2 flux)\n'
                            f"4. Retreat (-{enemy['attack_power']} HP)\n"
                            f'0. Check inventory\n')
        if user_choice in ['1', '2', '3', '4', '0']:
            return user_choice
        else:
            print("I don't understand your order, captain! Please try again.")


def attempt_repair_kit(character: dict) -> None:
    """
    Attempt ship repair

    :param character: A dictionary
    :precondition: Character must be a dictionary created by the create_character() function
    :postcondition: Attempt to repair the characters ship
    """
    if type(character) is not dict:
        raise TypeError("Arguments must be correct data types")
    if character['inventory']['repair_kits'] > 0:
        character['inventory']['repair_kits'] -= 1
        repair_ship(character)
    else:
        print(f"You do not have any repair kits, captain! Please try again.")


def attempt_air_barrage(character: dict, enemy: dict) -> None:
    """
    Attempt air barrage

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: Character must be a dictionary created by the create_character() function
    :precondition: Enemy must be a dictionary created by the generate_enemy_ship() or generate_boss() functions
    :postcondition: Attempt an air barrage attack
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    if character['inventory']['flux'] >= 2:
        character['inventory']['flux'] -= 2
        air_barrage(character, enemy)
    else:
        print(f"You do not have enough flux to use this ability, captain! Please try again.")


def attempt_retreat(character: dict, enemy: dict) -> bool:
    """
    Attempt retreat

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: Character must be a dictionary created by the create_character() function
    :precondition: Enemy must be a dictionary created by the generate_enemy_ship() or generate_boss() functions
    :postcondition: Attempt to retreat from battle
    :return: Success or failed retreat attempt as a boolean
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    retreat(character, enemy)
    if enemy['type'] == 'regular':
        return True
    else:
        return False


def user_battle_selection(character, enemy):
    """
    Execute user battle selection

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() or generate_boss() functions
    :postcondition: Execute the users battle choice
    :return: A boolean representing whether the user retreated or not
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    while True:
        choice = get_user_battle_choice(enemy)
        if choice == '0':
            check_inventory(character)
            continue
        elif choice == '1':
            fire_cannons(character, enemy)
        elif choice == '2':
            attempt_repair_kit(character)
        elif choice == '3':
            attempt_air_barrage(character, enemy)
        elif choice == '4':
            retreated = attempt_retreat(character, enemy)
            return retreated
        return False


def fire_cannons(character: dict, enemy: dict) -> None:
    """
    Fire cannons

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() or generate_boss() functions
    :postcondition: Fire cannons at enemy ship
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    if roll_critical_hit():
        enemy['health'] -= character['attack_power'] * 2
        print(f"You fire your cannons at {enemy['name']}. It's a critical hit!"
              f" They have {enemy['health']} health remaining.")
    else:
        enemy['health'] -= character['attack_power']
        print(f"You fire your cannons at {enemy['name']}. They have {enemy['health']} health remaining.")


def repair_ship(character: dict) -> None:
    """
    Repair ship

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Repair ship by half of max health
    >>> character_test = {'max_health': 100, 'health': 50}
    >>> repair_ship(character_test)
    You repair your ship and gain 50 health.
    """
    if type(character) is not dict:
        raise TypeError("Arguments must be correct data types")
    if character['health'] + (character['max_health'] / 2) > character['max_health']:
        character['health'] = character['max_health']
    else:
        character['health'] += int((character['max_health'] / 2))
    print(f"You repair your ship and gain {int((character['max_health'] / 2))} health.")


def air_barrage(character: dict, enemy: dict) -> None:
    """
    Use air barrage

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() or generate_boss() functions
    :postcondition: Use air barrage ability
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    if roll_critical_hit():
        enemy['health'] -= character['ability_power'] * 2
        print(f"You fire your air barrage at {enemy['name']}."
              f" It's a critical hit! The damage was absolutely devastating!\n"
              f"{enemy['name']} has {enemy['health']} health remaining.")
    else:
        enemy['health'] -= character['ability_power']
        print(f"You fire your air barrage at {enemy['name']}."
              f" It deals massive damage! They have {enemy['health']} health remaining.")


def retreat(character: dict, enemy: dict) -> None:
    """
    Retreat from battle

    :param character: A dictionary
    :param enemy: A dictionary

    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() or generate_boss() functions
    :postcondition: Retreat from battle and lose health
    >>> character_test = {'health': 100}
    >>> enemy_test = {'type': 'boss', 'attack_power': 10}
    >>> retreat(character_test, enemy_test)
    You cannot retreat from a boss battle, captain!
    >>> character_test = {'health': 100}
    >>> enemy_test = {'type': 'regular', 'attack_power': 10}
    >>> retreat(character_test, enemy_test)
    You retreat from the battle. The enemy fires several shots as you flee. You lose 10 health.
    You have 90 health remaining.
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    if enemy['type'] == 'boss':
        print(f"You cannot retreat from a boss battle, captain!")
    else:
        character['health'] -= enemy['attack_power']
        print(f"You retreat from the battle. The enemy fires several shots as you flee."
              f" You lose {enemy['attack_power']} health.\n"
              f"You have {character['health']} health remaining.")


def roll_critical_hit() -> bool:
    """
    Roll for critical hit

    :return: A boolean representing whether the roll was a critical hit or not
    """
    if random.randint(2, 10) <= 2:
        return True
    else:
        return False


def enemy_attack(character: dict, enemy: dict) -> None:
    """
    Execute enemy attack

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Execute an enemy attack
    >>> character_test = {'health': 100}
    >>> enemy_test = {'attack_power': 20}
    >>> enemy_attack(character_test, enemy_test)
    The enemy ship fires its cannons at you. You lose 20 health. You have 80 health remaining.
    >>> character_test
    {'health': 80}
    """
    if type(character) is not dict or type(enemy) is not dict:
        raise TypeError("Arguments must be correct data types")
    character['health'] -= enemy['attack_power']
    print(f'The enemy ship fires its cannons at you. You lose {enemy["attack_power"]} health.'
          f' You have {character["health"]} health remaining.')
