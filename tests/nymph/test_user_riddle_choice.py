"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from nymph import user_riddle_choice
from unittest.mock import patch


class TestUserRiddleChoice(TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_user_riddle_choice_correct(self, _):
        riddle = ["What can you find at the end of a rainbow?", "1. Absolutely nothing!", "2. A leprechaun's gold",
                  "3. The letter 'w'", "4. A 7th colour", '3']
        self.assertEqual(True, user_riddle_choice(riddle))

    @patch('builtins.input', side_effect=['1'])
    def test_user_riddle_choice_incorrect(self, _):
        riddle = ["What can you find at the end of a rainbow?", "1. Absolutely nothing!", "2. A leprechaun's gold",
                  "3. The letter 'w'", "4. A 7th colour", '3']
        self.assertEqual(False, user_riddle_choice(riddle))

    @patch('builtins.input', side_effect=['test'])
    def test_user_riddle_choice_incorrect_not_a_number(self, _):
        riddle = ["What can you find at the end of a rainbow?", "1. Absolutely nothing!", "2. A leprechaun's gold",
                  "3. The letter 'w'", "4. A 7th colour", '3']
        self.assertEqual(False, user_riddle_choice(riddle))
