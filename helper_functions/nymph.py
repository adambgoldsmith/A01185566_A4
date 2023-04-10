"""
Adam Goldsmith
A01185566
"""
import random


def nymph(character: dict) -> None:
    """
    Start nymph event

    :param character: A dictionary
    :preconditon: Character must be a dictionary created by the create_character() function
    :postcondition: Commence the nymph event
    """
    if type(character) is not dict:
        raise TypeError("Arguments must be correct data types")
    print()
    print(f"-------------------------\n"
          f"You notice a small sky-island as you drift through the air.\n"
          f"You dock your ship and cross over to the island.\n"
          f"A small cloud nymph is standing beneath some trees, dancing and singing.\n"
          f"The nymph approaches playfully and chants to you:\n"
          f"\"Solve my riddle and rewarded thee shall be! Falter in riposte and a trick you will see!\"\n")
    riddle = generate_riddle()
    tell_riddle(riddle)
    answer = user_riddle_choice(riddle)
    if answer:
        correct_answer(character)
    else:
        incorrect_answer(character)


def generate_riddle() -> list:
    """
    Generate riddle

    :return: A list of the generated riddle and its answers
    """
    riddles = {
        1: ["What can you find at the end of a rainbow?",
            "1. Absolutely nothing!",
            "2. A leprechaun's gold",
            "3. The letter 'w'",
            "4. A 7th colour",
            '3'],
        2: ["What is the 7th letter of the alphabet?",
            '1. H',
            '2. G',
            '3. ñ',
            '4. E',
            '1'],
        3: ["What must be broken before it is used?",
            '1. The law',
            '2. A new pair of boots',
            '3. A jar of honey',
            '4. An egg',
            '4'],
        4: ["What month of the year has 28 days?",
            '1. January',
            '2. February',
            '3. None of them!',
            '4. All of them!',
            '4'],
        5: ["What is full of holes but still holds water?",
            '1. A bucket',
            '2. A sponge',
            '3. A piece of cheese',
            '4. A watering can',
            '2'],
        6: ["I'm light as a feather, yet the strongest person can't hold me for five minutes. What am I?",
            '1. The moon',
            '2. Your breath',
            '3. A fly',
            '4. Smoke',
            '2'],
    }
    return riddles[random.randint(1, 6)]


def tell_riddle(riddle: list) -> None:
    """
    Tell riddle

    :param riddle: A list
    :precondition: riddle must be a list created by the generate_riddle() function
    :postcondition: print the riddle
    >>> test_riddle = ['riddle', 'answer one', 'red herring', 'red herring', 'answer', 'answer index']
    >>> tell_riddle()
    riddle
    red herring
    red herring
    red herring
    answer
    """
    if type(riddle) is not list:
        raise TypeError("Arguments must be correct data types")
    for phrase in range(5):
        print(riddle[phrase])


def user_riddle_choice(riddle: list) -> bool:
    """
    Get user riddle choice

    :param riddle: A list
    :precondition: riddle must be a list created by the generate_riddle() function
    :postcondition: Get the users riddle choice and check if it is correct
    :return: A boolean value representing if the user got the riddle correct
    """
    if type(riddle) is not list:
        raise TypeError("Arguments must be correct data types")
    user_choice = input()
    if user_choice == riddle[5]:
        return True
    else:
        return False


def incorrect_answer(character: dict) -> None:
    """
    Fail riddle

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: print dialogue and remove 25 gold from character inventory
    """
    if type(character) is not dict:
        raise TypeError("Arguments must be correct data types")
    print(f"\"No no no!\" the nypmph groans.\n"
          f"The nymph snaps it's fingers and a fresh fritzberry pie appears in their hand out of thin air.\n"
          f"In a split second, the nymph splats the fritzberry pie directly into your face!\n"
          f"The nymph sticks it's tongue out at you before flying away.")
    if character['inventory']['gold'] >= 25:
        character['inventory']['gold'] -= 25
        print("You check your pockets and notice 25 gold coins have been stolen.")
    print("You head back to your ship empty handed... And quite sticky...")


def correct_answer(character: dict) -> None:
    """
    Pass riddle

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: print dialogue and give the character 50 gold
    """
    if type(character) is not dict:
        raise TypeError("Arguments must be correct data types")
    character['inventory']['gold'] += 50
    print(f"\"CORRECT!\" the nymph giggles.\n"
          f"\"A promise is a promise!\"\n"
          f"The nymph hands you a small leather pouch filled with 50 gold coins!\n"
          f"You head back to your ship with a grin.")
