"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.character import check_if_achieved_goal


class TestCheckIfAchievedGoal(TestCase):
    def test_check_if_achieved_goal_true(self):
        board = {(0, 0): 'empty', (0, 1): 'empty', (1, 0): 'empty', (1, 1): 'empty'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        self.assertEqual(True, check_if_achieved_goal(board, character))

    def test_check_if_achieved_goal_false(self):
        board = {(0, 0): 'empty', (0, 1): 'empty', (1, 0): 'empty', (1, 1): 'empty'}
        character = {'X-coordinate': 0, 'Y-coordinate': 1}
        self.assertEqual(False, check_if_achieved_goal(board, character))
