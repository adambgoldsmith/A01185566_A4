"""
Adam Goldsmith
A01185566
"""
from events import *
from lore import *
from board import *


def game() -> None:
    """
    Create game loop
    """
    print_intro_lore()
    character = create_character()
    regions_cleared = 0
    while regions_cleared < 3:
        rows = 5
        columns = 5
        region = get_region(regions_cleared)
        board = create_board(rows, columns)
        achieved_goal = False
        while not achieved_goal:
            display_region(region)
            display_board(rows=rows, columns=columns, character=character)
            describe_current_location(region)
            display_stats(character)
            direction = get_user_choice(character)
            valid_move = validate_move(board, character, direction)
            if valid_move:
                move_character(character, direction)
                all_events(board, character, region)
                if not is_alive(character):
                    break
                level_up(character)
                achieved_goal = check_if_achieved_goal(board, character)
            else:
                print(f"You cannot go that way, captain! Please try again.")
        regions_cleared += 1
        if not is_alive(character):
            break
    if is_alive(character):
        print_end_lore()
    else:
        print(f"\n\nYour airship has been destroyed... Game over.")


def main():
    """
    Drive the program
    """
    game()


if __name__ == '__main__':
    main()
