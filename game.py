"""
Adam Goldsmith
A01185566
"""
from helper_functions.events import all_events
from helper_functions.lore import print_intro_lore
from helper_functions.lore import print_end_lore
from helper_functions.lore import get_region
from helper_functions.board import create_board
from helper_functions.board import display_region
from helper_functions.board import display_board
from helper_functions.board import describe_current_location
from helper_functions.board import get_user_choice
from helper_functions.board import validate_move
from helper_functions.board import move_character
from helper_functions.character import create_character
from helper_functions.character import is_alive
from helper_functions.character import level_up
from helper_functions.character import check_if_achieved_goal
from helper_functions.character import display_stats


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
            display_board(rows, columns, character)
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
