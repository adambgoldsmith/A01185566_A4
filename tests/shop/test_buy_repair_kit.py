"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from shop import buy_repair_kit
from unittest.mock import patch


class TestBuyRepairKit(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_repair_kit_output(self, mock_output):
        character = {'inventory': {
            'repair_kits': 0,
            'gold': 30
        }}
        buy_repair_kit(character)
        buy_repair_kit_output = mock_output.getvalue()
        expected_output = "You bought a repair kit for 30 gold.\n\n"
        self.assertEqual(expected_output, buy_repair_kit_output)

    def test_buy_repair_kit_gold_taken(self):
        character = {'inventory': {
            'repair_kits': 0,
            'gold': 30
        }}
        buy_repair_kit(character)
        self.assertEqual(0, character['inventory']['gold'])

    def test_buy_repair_kit_repair_kit_added(self):
        character = {'inventory': {
            'repair_kits': 0,
            'gold': 30
        }}
        buy_repair_kit(character)
        self.assertEqual(1, character['inventory']['repair_kits'])
