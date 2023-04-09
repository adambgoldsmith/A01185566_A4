import io
from unittest import TestCase
from board import get_user_choice
from unittest.mock import patch

class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['north'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_valid_output(self, mock_output, _):
        character = {}
        get_user_choice(character)
        get_user_choice_output = mock_output.getvalue()
        expected_output = 'Which direction will you travel?\n1. north\n2. south\n3. east\n4. west\n0. inventory\n'
        self.assertEqual(expected_output, get_user_choice_output)

    @patch('builtins.input', side_effect=['sworthst', 'north'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_to_valid_output(self, mock_output, _):
        character = {}
        get_user_choice(character)
        get_user_choice_output = mock_output.getvalue()
        expected_output = 'Which direction will you travel?\n'\
                          '1. north\n2. south\n3. east\n4. west\n0. inventory\n'\
                          'That is not a valid direction! Please try again.\n'\
                          'Which direction will you travel?\n'\
                          '1. north\n2. south\n3. east\n4. west\n0. inventory\n'
        self.assertEqual(expected_output, get_user_choice_output)

    @patch('builtins.input', side_effect=['north'])
    def test_get_user_choice_north(self, _):
        character = {}
        result = get_user_choice(character)
        self.assertEqual('north', result)

    @patch('builtins.input', side_effect=['south'])
    def test_get_user_choice_south(self, _):
        character = {}
        result = get_user_choice(character)
        self.assertEqual('south', result)

    @patch('builtins.input', side_effect=['east'])
    def test_get_user_choice_east(self, _):
        character = {}
        result = get_user_choice(character)
        self.assertEqual('east', result)

    @patch('builtins.input', side_effect=['west'])
    def test_get_user_choice_west(self, _):
        character = {}
        result = get_user_choice(character)
        self.assertEqual('west', result)