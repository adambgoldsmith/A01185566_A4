"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from battle import fire_cannons
from unittest.mock import patch


class TestFireCannons(TestCase):
    @patch('battle.roll_critical_hit', side_effect=[False])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fire_cannons_regular_output(self, mock_output, _):
        character = {'attack_power': 10}
        enemy = {'health': 100, 'name': 'the pirate ship'}
        fire_cannons(character, enemy)
        fire_cannons_output = mock_output.getvalue()
        expected_output = "You fire your cannons at the pirate ship. They have 90 health remaining.\n"
        self.assertEqual(expected_output, fire_cannons_output)

    @patch('battle.roll_critical_hit', side_effect=[True])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fire_cannons_critical_hit_output(self, mock_output, _):
        character = {'attack_power': 10}
        enemy = {'health': 100, 'name': 'the pirate ship'}
        fire_cannons(character, enemy)
        fire_cannons_output = mock_output.getvalue()
        expected_output = "You fire your cannons at the pirate ship. It's a critical hit! They have 80" \
                          " health remaining.\n"
        self.assertEqual(expected_output, fire_cannons_output)

    @patch('battle.roll_critical_hit', side_effect=[False])
    def test_fire_cannons_regular_damage(self, _):
        character = {'attack_power': 10}
        enemy = {'health': 100, 'name': 'the pirate ship'}
        fire_cannons(character, enemy)
        self.assertEqual(90, enemy['health'])

    @patch('battle.roll_critical_hit', side_effect=[True])
    def test_fire_cannons_critical_hit_damage(self, _):
        character = {'attack_power': 10}
        enemy = {'health': 100, 'name': 'the pirate ship'}
        fire_cannons(character, enemy)
        self.assertEqual(80, enemy['health'])
