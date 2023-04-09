"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from battle import air_barrage
from unittest.mock import patch


class TestAirBarrage(TestCase):
    @patch('battle.roll_critical_hit', side_effect=[False])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_air_barrage_regular_output(self, mock_output, _):
        character = {'ability_power': 20}
        enemy = {'name': 'the pirate ship', 'health': 100}
        air_barrage(character, enemy)
        air_barrage_output = mock_output.getvalue()
        expected_output = "You fire your air barrage at the pirate ship. It deals massive damage! " \
                          "They have 80 health remaining.\n"
        self.assertEqual(expected_output, air_barrage_output)

    @patch('battle.roll_critical_hit', side_effect=[True])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_air_barrage_critical_hit_output(self, mock_output, _):
        character = {'ability_power': 20}
        enemy = {'name': 'the pirate ship', 'health': 100}
        air_barrage(character, enemy)
        air_barrage_output = mock_output.getvalue()
        expected_output = "You fire your air barrage at the pirate ship. It's a critical hit! The damage was" \
                          " absolutely devastating!\n" \
                          "the pirate ship has 60 health remaining.\n"
        self.assertEqual(expected_output, air_barrage_output)

    @patch('battle.roll_critical_hit', side_effect=[False])
    def test_air_barrage_regular_damage(self, _):
        character = {'ability_power': 20}
        enemy = {'name': 'the pirate ship', 'health': 100}
        air_barrage(character, enemy)
        self.assertEqual(80, enemy['health'])

    @patch('battle.roll_critical_hit', side_effect=[True])
    def test_air_barrage_critical_hit_damage(self, _):
        character = {'ability_power': 20}
        enemy = {'name': 'the pirate ship', 'health': 100}
        air_barrage(character, enemy)
        self.assertEqual(60, enemy['health'])
