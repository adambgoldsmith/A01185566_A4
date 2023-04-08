from battle import *
from character import *

def boss_battle(character: dict, region: list) -> None:
    """
    Start boss battle

    :param character: A dictionary
    :param region: A list
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: region must be a list created by the get_region() function
    :postcondition: Commence a boss battle sequence
    """
    print('-------------------------')
    boss = generate_boss(region)
    boss_description(boss, region)
    print(f"{boss['name']} has {boss['health']} health and {boss['attack_power']} attack power.")
    while boss['health'] > 0:
        user_battle_choice(character, boss)
        if boss['health'] > 0:
            boss_attack(character, boss)
            if not is_alive(character):
                break
    if boss['health'] <= 0:
        character['experience'] += 100
        character['health'] = character['max_health']
        print(f"{boss['name']} falls, plunging through the clouds. You have emerged victorious!\n"
              f"You feel invigorated by your victory. You gain 100 experience points for conquering such a formidable foe!\n"
              f"You continue on your journey...")

def boss_description(boss: dict, region: list) -> None:
    """
    Print boss description

    :param boss: A dictionary
    :param region: A list
    :precondition: boss must be a dictionary created by the generate_boss() function
    :precondition: Region must be a list created by the get_region() function
    :postcondition: print a description of the boss
    """
    print(f"As you near the far reaches of {region[0]} you sense the presence of an immense darkness.\n"
          f"From beneath the clouds, {boss['name']}, swoops into view and blocks your path.\n"
          f"You prepare for a tough battle...")
    
def generate_boss(region: list) -> dict:
    """
    Generate boss

    :param region: A list
    :precondition: Region must be a list created by the get_region() function
    :postcondition: generate a boss based on the region
    :return: A dictionary representing a boss
    """
    boss_one = {
        'type': 'boss',
        'name': 'Odeza, The Venom Wyvern',
        'health': 150,
        'attack_power': 10,
        'attack_desc': 'sweeps her tail towards you',
        'ability_power': 25,
        'prepared': False,
        'ability_desc': 'blows a huge cloud of noxious venom at you',
    }
    boss_two = {
        'type': 'boss',
        'name': 'Nebulous, The Mist Colossus',
        'health': 250,
        'attack_power': 15,
        'attack_desc': 'swings his colossal mace at you',
        'ability_power': 30,
        'prepared': False,
        'ability_desc': 'raises his mace high above his head and brings it down with a thunderous crash',
    }
    boss_three = {
        'type': 'boss',
        'name': 'F̵͍̺̺͕̩͍̼̀ͥ̒O̹̞̹ͫ͒͝L̝̟͔̣̦͔̖̥͊̀ͥ̄͟G̩͇̣̱̮͍͑͞R͇̦̘͖̣̞͖ͪ̐̈́̏͞I̸̹̺̰̥̤̜̯̭̿̄ͩM̨͚͎̜̬ͤ̎̏͒, The Void Kraken',
        'health': 500,
        'attack_power': 35,
        'attack_desc': 'grapples its tentacles around your ship and squeezes tight',
        'ability_power': 50,
        'prepared': False,
        'ability_desc': 'opens its maw and unleashes a torrent of void energy',
    }
    if region[0] == 'The Cloud Expanse':
        return boss_one
    elif region[0] == 'Fogmourne':
        return boss_two
    elif region[0] == 'The Void Isles':
        return boss_three
    else:
        raise ValueError(f'Invalid region.')

def boss_attack(character: dict, boss: dict) -> None:
    """
    Execute boss attack

    :param character: A dictionary
    :param boss: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :precondition: boss must be a dictionary created by the generate_boss() function
    :postcondition: execute a boss attack
    """
    attack_type = random.randint(1, 4)
    if attack_type == 1 and boss['prepared'] == False:
        boss['prepared'] = True
        print(f"{boss['name']} gets ready to unleash a powerful attack!")
    elif boss['prepared'] == True:
        character['health'] -= boss['ability_power']
        print(f"{boss['name']} has unleashed a powerful attack!")
        print(f"{boss['name']} {boss['ability_desc']}. It dealt {boss['ability_power']} damage! You have {character['health']} health remaining.")
        boss['prepared'] = False
    else:
        character['health'] -= boss['attack_power']
        print(f"{boss['name']} {boss['attack_desc']}. It dealt {boss['attack_power']} damage! You have {character['health']} health remaining.")
