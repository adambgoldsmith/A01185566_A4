"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from shop import shop
from unittest.mock import patch


class TestShop(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shop(self, mock_output):
        character = {'inventory': {
            'flux': 0,
            'repair_kits': 0,
            'gold': 50
        }}
        shop(character)
        shop_output = mock_output.getvalue()
        expected_output = ""
        self.assertEqual(expected_output, shop_output)
