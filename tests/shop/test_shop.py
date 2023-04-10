"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.shop import shop
from unittest.mock import patch


class TestShop(TestCase):
    @patch('helper_functions.shop.user_shop_choice', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_shop(self, mock_output, _):
        character = {'inventory': {
            'flux': 0,
            'repair_kits': 0,
            'gold': 50
        }}
        shop(character)
        shop_output = mock_output.getvalue()
        expected_output = "-------------------------\n" \
                          "You notice a small trade ship gliding through the air. The large wooden propeller on its" \
                          " roof clicks loudly with each rotation.\n" \
                          "You float up next to the ship, dock, and climb aboard.\n" \
                          "A grubby, short, hobgoblin shop keeper welcomes you in...\n"
        self.assertEqual(expected_output, shop_output)

    def test_user_shop_type_error(self):
        with self.assertRaises(TypeError):
            shop(None)