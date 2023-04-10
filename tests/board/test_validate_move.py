"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.board import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_valid(self):
        board = {(0, 0): 'empty', (0, 1): 'empty', (1, 0): 'empty', (1, 1): 'empty'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = 'south'
        self.assertEqual(True, validate_move(board, character, direction))

    def test_validate_move_invalid(self):
        board = {(0, 0): 'empty', (0, 1): 'empty', (1, 0): 'empty', (1, 1): 'empty'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        direction = 'north'
        self.assertEqual(False, validate_move(board, character, direction))
