"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.battle import retreat
from unittest.mock import patch


class TestRetreat(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_retreat_regular(self, mock_output):
        character = {'health': 100}
        enemy = {'type': 'regular', 'attack_power': 10}
        retreat(character, enemy)
        retreat_output = mock_output.getvalue()
        expected_output = "You retreat from the battle. The enemy fires several shots as you flee." \
                          " You lose 10 health.\n" \
                          "You have 90 health remaining.\n"
        self.assertEqual(expected_output, retreat_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_retreat_boss(self, mock_output):
        character = {'health': 100}
        enemy = {'type': 'boss', 'attack_power': 10}
        retreat(character, enemy)
        retreat_output = mock_output.getvalue()
        expected_output = "You cannot retreat from a boss battle, captain!\n"
        self.assertEqual(expected_output, retreat_output)

    def test_retreat_damage_taken(self):
        character = {'health': 100}
        enemy = {'type': 'regular', 'attack_power': 10}
        retreat(character, enemy)
        self.assertEqual(90, character['health'])
