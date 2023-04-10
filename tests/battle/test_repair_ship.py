"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.battle import repair_ship
from unittest.mock import patch


class TestRepairShip(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_repair_ship_output(self, mock_output):
        character = {'health': 50, 'max_health': 120}
        repair_ship(character)
        repair_ship_output = mock_output.getvalue()
        expected_value = "You repair your ship and gain 60 health.\n"
        self.assertEqual(expected_value, repair_ship_output)

    def test_repair_ship_less_than_max(self):
        character = {'health': 50, 'max_health': 100}
        repair_ship(character)
        self.assertEqual(100, character['health'])

    def test_repair_ship_max(self):
        character = {'health': 100, 'max_health': 100}
        repair_ship(character)
        self.assertEqual(100, character['health'])

    def test_repair_ship_type_error(self):
        with self.assertRaises(TypeError):
            repair_ship(None)
