"""
Adam Goldsmith
A01185566
"""
import random


def chest(character: dict) -> None:
    """
    Start chest event

    :param character: A dictionary
    :precondition: character must be a dictionary created by the create_character() function
    :postcondition: Commence the chest event
    """
    print(f"-------------------------")
    print(f"Out of the corner of your eye you spot a shimmering chest on a tiny floating island.\n"
          f"You approach the chest and notice several gemstones of differing shapes above the heavy iron latch.")
    puzzle_answer = generate_puzzle()
    user_answer = user_puzzle_choice()
    if user_answer == puzzle_answer:
        character['inventory']['gold'] += 50
        print(f"You hear a loud click. The chest swings open to reveal 50 gold coins!"
              f" You collect your spoils and head back to your ship.")
    else:
        print(f"That doesn't look right. The gemstones fade of their colours."
              f" You head back to your ship empty handed...")


def generate_pattern() -> str:
    """
    Generate chest puzzle

    **Note: This function is not complete. It is a work in progress.**
    """
    pattern = ""
    for _ in range(6):
        gem = random.choice(['topaz', 'emerald', 'ruby', 'sapphire'])
        if gem == 'topaz':
            pattern += "O"
        elif gem == 'emerald':
            pattern += "X"
        elif gem == 'ruby':
            pattern += "I"
        else:
            pattern += "V"
    return pattern


def generate_puzzle() -> str:
    """
    Generate chest puzzle

    :return: Answer as a string
    """
    pattern = generate_pattern()
    full_pattern = pattern * 2
    take_away = random.randint(2, 5)
    missing_pattern = full_pattern[:len(full_pattern) - take_away]
    print(missing_pattern)
    answer = full_pattern[len(full_pattern) - take_away]
    return answer


def user_puzzle_choice() -> str:
    """
    Get user answer

    :return: User answer as a string
    """
    user_choice = input(f"What is the next gemstone in the pattern?\n"
                        f"1. O (topaz)\n"
                        f"2. X (emerald)\n"
                        f"3. I (ruby)\n"
                        f"4. V (sapphire)\n")
    if user_choice == "1":
        return "O"
    elif user_choice == "2":
        return "X"
    elif user_choice == "3":
        return "I"
    elif user_choice == "4":
        return "V"
    else:
        return "incorrect"
