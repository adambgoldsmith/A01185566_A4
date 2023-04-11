"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.battle import attempt_retreat
from unittest.mock import patch


class TestAttemptRetreat(TestCase):
    @patch('helper_functions.battle.retreat', side_effect=[None])
    def test_attempt_retreat_regular(self, _):
        character = {}
        enemy = {'type': 'regular'}
        self.assertEqual(True, attempt_retreat(character, enemy))

    @patch('helper_functions.battle.retreat', side_effect=[None])
    def test_attempt_retreat_boss(self, _):
        character = {}
        enemy = {'type': 'boss'}
        self.assertEqual(False, attempt_retreat(character, enemy))

    def test_attempt_retreat_type_error(self):
        with self.assertRaises(TypeError):
            attempt_retreat(None, None)
