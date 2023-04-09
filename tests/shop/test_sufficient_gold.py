import io
from unittest import TestCase
from shop import sufficient_gold
from unittest.mock import patch


class TestSufficientGold(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sufficient_gold_flux_sufficient_output(self, mock_output):
        character = {'inventory': {
            'flux': 0,
            'gold': 100
        }}
        sufficient_gold('1', character)
        sufficient_gold_output = mock_output.getvalue()
        expected_output = "You bought 2 flux for 10 gold.\n\n"
        self.assertEqual(expected_output, sufficient_gold_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sufficient_gold_repair_kit_sufficient_output(self, mock_output):
        character = {'inventory': {
            'repair_kits': 0,
            'gold': 100
        }}
        sufficient_gold('2', character)
        sufficient_gold_output = mock_output.getvalue()
        expected_output = "You bought a repair kit for 30 gold.\n\n"
        self.assertEqual(expected_output, sufficient_gold_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sufficient_gold_flux_insufficient_output(self, mock_output):
        character = {'inventory': {
            'flux': 0,
            'gold': 9
        }}
        sufficient_gold('1', character)
        sufficient_gold_output = mock_output.getvalue()
        expected_output = "You don't have enough gold, friend.\n\n"
        self.assertEqual(expected_output, sufficient_gold_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sufficient_gold_repair_kit_insufficient_output(self, mock_output):
        character = {'inventory': {
            'repair_kits': 0,
            'gold': 29
        }}
        sufficient_gold('2', character)
        sufficient_gold_output = mock_output.getvalue()
        expected_output = "You don't have enough gold, friend.\n\n"
        self.assertEqual(expected_output, sufficient_gold_output)
