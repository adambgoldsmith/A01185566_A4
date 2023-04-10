from unittest import TestCase
from helper_functions.boss import boss_battle_loop
from unittest.mock import patch


class TestBossBattleLoop(TestCase):
    @patch('boss.user_battle_selection', side_effect=[None])
    @patch('boss.boss_attack', side_effect=[None])
    @patch('boss.is_alive', side_effect=[True])
    def test_boss_battle_loop_character_alive(self, _, __, ___):
        character = {}
        boss = {}
        boss_battle_loop(character)
        self.assertEqual(None, )
