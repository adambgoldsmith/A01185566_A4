def create_board(columns, rows):
    """
    Generate game board

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows must be a positive integer that is greater than or equal to 2
    :precondition: columns must be a positive integer that is greater than or equal to 2
    :postcondition: creates a dictionary of board coordinates with a random room assigned to each space.
    :return: the game board as a dictionary.
    """
    events = [] # Add events here
    board = {}
    if rows < 2 or columns < 2:
        raise ValueError("Board dimensions must be 5 or greater")
    for row in range(rows):
        for column in range(columns):
            board[(column, row)] = 'aa' # Add event name here
    return board


def create_character():
    character = {
        'X-coordinate': 0,
        'Y-coordinate': 0,
        'name': 'Captain Magnus Selwood', # Add custom name?
        'level': 1,
        'experience': 0,
        'max_health': 100,
        'health': 100,
        'attack_power': 10,
        'defense': 10,
        'inventory': [],
        # Add abilities?
    }
    return character

def display_board(rows, columns, character):
    """
    Display board

    :param rows: A positive integer
    :param columns: A positive integer
    :param character: A dictionary
    :precondition: rows must be a positive integer greater than or equal to 2
    :precondition: columns must be a positive integer greater than or equal to 2
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

def describe_current_location(board, character):
    pass

def get_user_choice():
    """
    Get direction input

    :return: the user's desired direction as a string
    """
    print("Which direction will you go?")
    print("1. north\n2. south\n3. east\n4. west")
    options = ['1', '2', '3', '4', 'north', 'south', 'east', 'west']
    while True:
        user_input = input().lower()
        if user_input in options:
            return user_input
        else:
            print("That is not a valid direction! Please try again.")

def validate_move(board, character, direction):
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
    
def move_character(character, direction):
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

def get_event(board, character):
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    event = board[character_location]
    return event

def activate_event(event, character):
    character['experience'] += 25
    print("You gain 25 experience points for succeeding!\n")

def level_up(character):
    if character['experience'] >= 100:
        character['level'] += 1
        character['experience'] = 0
        character['max_health'] += 10
        character['health'] += 10 # change how much health is gained?
        character['attack_power'] += 5
        character['defense'] += 5
        print("You have leveled up! Your ship's cannons are now stronger and your hull has been reinforced!\n"
              f"You are now level {character['level']}")


def check_if_achieved_goal(board, character):
    """
    Check if goal attained

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board must be a dictionary created by make_board() function
    :precondition: character must be a dictionary created by the make_character() function
    :postcondition: verify if player has reached the goal
    :return: verification if player has reached the goal as a boolean
    """
    character_location = (character['X-coordinate'], character['Y-coordinate'])
    if character_location == list(board.keys())[-1]:
        return True
    else:
        return False

def game():
    rows = 5
    columns = 5
    board = create_board(rows, columns)
    # user_name = input("What is your name, adventurer? ") # Turn into user info function?
    character = create_character() # Pass in user_info?
    achieved_goal = False
    # print lore here
    while not achieved_goal:
        display_board(rows=rows, columns=columns, character=character)
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            event = get_event(board, character)
            if event != False:
                activate_event(event, character) # Event should give experience
                level_up(character)
            achieved_goal = check_if_achieved_goal(board, character)
        else:
            print("You cannot go that way!")
    print('You have achieved your goal! Congratulations!')



def main():
    game()

if __name__ == '__main__':
    main()