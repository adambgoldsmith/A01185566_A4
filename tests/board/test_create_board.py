"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.board import create_board
from unittest.mock import patch


class TestCreateBoard(TestCase):
    @patch('random.choice', side_effect=['empty', 'shop', 'empty', 'empty', 'empty', 'empty',
                                         'nymph', 'empty', 'empty', 'chest', 'empty', 'empty',
                                         'empty', 'empty', 'empty', 'chest', 'shop', 'empty',
                                         'nymph', 'empty', 'empty', 'empty', 'empty'])
    @patch('board.create_events_list', side_effect=[['chest', 'chest', 'nymph', 'nymph', 'shop',
                                                     'shop', 'empty', 'empty', 'empty', 'empty',
                                                     'empty', 'empty', 'empty', 'empty', 'empty',
                                                     'empty', 'empty', 'empty', 'empty', 'empty', 'empty',
                                                     'empty', 'empty']])
    def test_create_board(self, _, __):
        expected_value = {(0, 0): 'start', (0, 1): 'empty', (0, 2): 'chest', (0, 3): 'empty',
                               (0, 4): 'empty', (1, 0): 'empty', (1, 1): 'empty', (1, 2): 'empty',
                               (1, 3): 'chest', (1, 4): 'empty', (2, 0): 'shop', (2, 1): 'nymph',
                               (2, 2): 'empty', (2, 3): 'shop', (2, 4): 'empty', (3, 0): 'empty',
                               (3, 1): 'empty', (3, 2): 'empty', (3, 3): 'empty', (3, 4): 'empty',
                               (4, 0): 'empty', (4, 1): 'empty', (4, 2): 'empty', (4, 3): 'nymph',
                               (4, 4): 'boss'}
        self.assertEqual(expected_value, create_board(5, 5))
