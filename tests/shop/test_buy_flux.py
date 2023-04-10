"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.shop import buy_flux
from unittest.mock import patch


class TestBuyFlux(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_flux_output(self, mock_output):
        character = {'inventory': {
            'flux': 0,
            'gold': 10
        }}
        buy_flux(character)
        buy_flux_output = mock_output.getvalue()
        expected_output = "You bought 2 flux for 10 gold.\n\n"
        self.assertEqual(expected_output, buy_flux_output)

    def test_buy_flux_gold_taken(self):
        character = {'inventory': {
            'flux': 0,
            'gold': 10
        }}
        buy_flux(character)
        self.assertEqual(0, character['inventory']['gold'])

    def test_buy_flux_flux_added(self):
        character = {'inventory': {
            'flux': 0,
            'gold': 10
        }}
        buy_flux(character)
        self.assertEqual(2, character['inventory']['flux'])
