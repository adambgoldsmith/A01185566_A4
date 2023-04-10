"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.chest import user_puzzle_choice
from unittest.mock import patch


class TestUserPuzzleChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_user_puzzle_choice_one(self, _):
        self.assertEqual('O', user_puzzle_choice())

    @patch('builtins.input', side_effect=['2'])
    def test_user_puzzle_choice_two(self, _):
        self.assertEqual('X', user_puzzle_choice())

    @patch('builtins.input', side_effect=['3'])
    def test_user_puzzle_choice_three(self, _):
        self.assertEqual('I', user_puzzle_choice())

    @patch('builtins.input', side_effect=['4'])
    def test_user_puzzle_choice_four(self, _):
        self.assertEqual('V', user_puzzle_choice())

    @patch('builtins.input', side_effect=['5'])
    def test_user_puzzle_choice_number_out_of_bounds(self, _):
        self.assertEqual('incorrect', user_puzzle_choice())

    @patch('builtins.input', side_effect=['test'])
    def test_user_puzzle_choice_not_a_number(self, _):
        self.assertEqual('incorrect', user_puzzle_choice())
