"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.character import level_up
from unittest.mock import patch


class TestLevelUp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_less_than_100_exp_output(self, mock_output):
        character = {
            'level': 1,
            'experience': 0,
            'max_health': 100,
            'health': 100,
            'attack_power': 10,
            'ability_power': 20,
        }
        level_up(character)
        level_up_output = mock_output.getvalue()
        expected_output = ""
        self.assertEqual(expected_output, level_up_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_100_exp_output(self, mock_output):
        character = {
            'level': 1,
            'experience': 100,
            'max_health': 100,
            'health': 100,
            'attack_power': 10,
            'ability_power': 20,
        }
        level_up(character)
        level_up_output = mock_output.getvalue()
        expected_output = "You have leveled up! Your ship's cannons are now stronger and your hull has been" \
                          " reinforced!\n" \
                          "You are now level 2! Your max health is now 120 and your attack power is now 15.\n" \
                          "Your health has been restored to 120.\n\n"
        self.assertEqual(expected_output, level_up_output)

    def test_level_up_greater_than_100_exp(self):
        character = {
            'level': 1,
            'experience': 150,
            'max_health': 100,
            'health': 100,
            'attack_power': 10,
            'ability_power': 20,
        }
        level_up(character)
        self.assertEqual({'level': 2,
                          'experience': 50,
                          'max_health': 120,
                          'health': 120,
                          'attack_power': 15,
                          'ability_power': 25}, character)

    def test_level_up_less_than_100_exp(self):
        character = {
            'level': 1,
            'experience': 85,
            'max_health': 100,
            'health': 100,
            'attack_power': 10,
            'ability_power': 20,
        }
        level_up(character)
        self.assertEqual({'level': 1,
                          'experience': 85,
                          'max_health': 100,
                          'health': 100,
                          'attack_power': 10,
                          'ability_power': 20}, character)
