"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.battle import battle_loop
from unittest.mock import patch


class TestBattleLoop(TestCase):
    @patch('itertools.cycle', side_effect=['character', 'enemy'])
    @patch('helper_functions.character.is_alive', side_effect=[True])
    def test_battle_loop_character_alive(self, _, __):
        character = {'health': 100}
        enemy = {'health': 0}
        self.assertEqual(None, battle_loop(character, enemy))

    @patch('itertools.cycle', side_effect=['character', 'enemy'])
    @patch('helper_functions.character.is_alive', side_effect=[False])
    def test_battle_loop_character_dead(self, _, __):
        character = {'health': 0}
        enemy = {'health': 0}
        self.assertEqual(None, battle_loop(character, enemy))

    def test_battle_loop_type_error(self):
        with self.assertRaises(TypeError):
            battle_loop(None, None)
