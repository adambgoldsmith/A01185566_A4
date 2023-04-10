from unittest import TestCase
from helper_functions.boss import boss_battle_loop
from unittest.mock import patch


class TestBossBattleLoop(TestCase):
    @patch('helper_functions.boss.user_battle_selection', side_effect=[None])
    @patch('helper_functions.boss.boss_attack', side_effect=[None])
    @patch('helper_functions.boss.is_alive', side_effect=[False])
    def test_boss_battle_loop_character_dead(self, _, __, ___):
        character = {}
        boss = {'health': 100}
        self.assertEqual(None, boss_battle_loop(character, boss))

    @patch('helper_functions.boss.user_battle_selection', side_effect=[None])
    @patch('helper_functions.boss.boss_attack', side_effect=[None])
    @patch('helper_functions.boss.is_alive', side_effect=[True])
    def test_boss_battle_loop_character_alive(self, _, __, ___):
        character = {}
        boss = {'health': 0}
        self.assertEqual(None, boss_battle_loop(character, boss))

    def test_boss_battle_loop_type_error(self):
        with self.assertRaises(TypeError):
            boss_battle_loop(None, None)
