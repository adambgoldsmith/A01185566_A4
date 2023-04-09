import random
from character import *

def battle(character: dict) -> None:
    """
    Start battle event

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Commence an enemy battle sequence
    """
    print(f"-------------------------")
    print(f"You spot a hostile air ship on the horizon. As the ship gets closer, your eyes are drawn to the large skull\n"
          f"and crossbones crudely painted on it's side. Pirates! You ready your cannons for battle.")
    enemy_ship = generate_enemy_ship()
    print(f"The enemy ship has {enemy_ship['health']} health and {enemy_ship['attack_power']} attack power.")
    while enemy_ship['health'] > 0:
        retreated = user_battle_choice(character, enemy_ship)
        if retreated:
            break
        if enemy_ship['health'] > 0:
            enemy_attack(character, enemy_ship)
            if not is_alive(character):
                break
    if enemy_ship['health'] <= 0:
        character['inventory']['gold'] += 50
        character['experience'] += 25
        print(f"The hostile ship plummets through the clouds and explodes in a fiery ball of flames. Well done, captain! You stand victorious!\n"
              f"You gain 50 gold coins for your victory.\n"
              f"You gain 25 experience points for your victory.")
    
def generate_enemy_ship() -> dict:
    """
    Generate enemy ship

    :return: A dictionary representing an enemy ship
    """
    enemy_ship = { # change with difficulty
        'type': 'regular',
        'name': 'the pirate ship',
        'health': 50, 
        'attack_power': 10,
    }
    return enemy_ship

def user_battle_choice(character: dict, enemy: dict) -> bool:
    """
    Get user battle choice

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Get user battle choice
    :return: A boolean representing whether the user retreated or not
    """
    while True:
        user_choice = input(f'What is your next move, captain?\n'
                            f'1. Fire cannons\n'
                            f'2. Repair ship (-1 repair kit)\n'
                            f'3. Air Barrage (-2 flux)\n'
                            f"4. Retreat (-{enemy['attack_power']} HP)\n"
                            f'0. Check inventory\n')
        if user_choice == '1':
            fire_cannons(character, enemy)
            break
        elif user_choice == '2':
            if character['inventory']['repair_kits'] > 0:
                character['inventory']['repair_kits'] -= 1
                repair_ship(character)
                break
            else:
                print(f"You do not have any repair kits, captain! Please try again.")
        elif user_choice == '3':
            if character['inventory']['flux'] >= 2:
                character['inventory']['flux'] -= 2
                air_barrage(character, enemy)
                break
            else:
                print(f"You do not have enough flux to use this ability, captain! Please try again.")
        elif user_choice == '4':
            retreat(character, enemy)
            if enemy['type'] == 'regular':
                return True
        elif user_choice == '0':
            check_inventory(character)
        else:
            print("I don't understand your order, captain! Please try again.")
    return False

def fire_cannons(character: dict, enemy: dict) -> None:
    """
    Fire cannons

    :param character: A dictionary
    :param enemy: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Fire cannons at enemy ship
    """
    if roll_critical_hit():
        enemy['health'] -= character['attack_power'] * 2
        print(f"You fire your cannons at {enemy['name']}. It's a critical hit! They have {enemy['health']} health remaining.")
    else:
        enemy['health'] -= character['attack_power']
        print(f"You fire your cannons at {enemy['name']}. They have {enemy['health']} health remaining.")

def repair_ship(character: dict) -> None:
    """
    Repair ship

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Repair ship by half of max health
    """
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
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Use air barrage ability
    """
    if roll_critical_hit():
        enemy['health'] -= character['ability_power'] * 2
        print(f"You fire your air barrage at {enemy['name']}. It's a critical hit! The damage was absolutely devastating!\n"
              f"{enemy['name']} has {enemy['health']} health remaining.")
    else:
        enemy['health'] -= character['ability_power']
        print(f"You fire your air barrage at {enemy['name']}. It deals massive damage! They have {enemy['health']} health remaining.")

def retreat(character: dict, enemy: dict) -> None:
    """
    Retreat from battle

    :param character: A dictionary
    :param enemy: A dictionary

    :precondition: character must be a dictionary created by the create_character() function
    :precondition: enemy must be a dictionary created by the generate_enemy_ship() function
    :postcondition: Retreat from battle and lose health
    """
    if enemy['type'] == 'boss':
        print(f"You cannot retreat from a boss battle, captain!")
    else:
        character['health'] -= enemy['attack_power']
        print(f"You retreat from the battle. The enemy fires several shots as you flee. You lose {enemy['attack_power']} health.\n"
              f"You have {character['health']} health remaining.")

def roll_critical_hit() -> bool:
    """
    Roll for critical hit

    :return: A boolean representing whether the roll was a critical hit or not
    """
    if random.randint(2, 10) <= 2: #######################
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
    """
    character['health'] -= enemy['attack_power']
    print(f'The enemy ship fires its cannons at you. You lose {enemy["attack_power"]} health. You have {character["health"]} health remaining.')
    