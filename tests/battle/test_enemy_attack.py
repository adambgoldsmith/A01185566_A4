"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.battle import enemy_attack
from unittest.mock import patch


class TestEnemyAttack(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_output(self, mock_output):
        character = {'health': 100}
        enemy = {'attack_power': 10}
        enemy_attack(character, enemy)
        enemy_attack_output = mock_output.getvalue()
        expected_output = "The enemy ship fires its cannons at you. You lose 10 health. You have 90 health remaining.\n"
        self.assertEqual(expected_output, enemy_attack_output)

    def test_enemy_attack_damage(self):
        character = {'health': 100}
        enemy = {'attack_power': 10}
        enemy_attack(character, enemy)
        self.assertEqual(90, character['health'])
