import io
from unittest import TestCase
from helper_functions.shop import user_shop_choice
from unittest.mock import patch


class TestUserShopChoice(TestCase):
    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_shop_choice_leave_output(self, mock_output, _):
        character = {'inventory': {'gold': 100}}
        user_shop_choice(character)
        user_shop_choice_output = mock_output.getvalue()
        expected_output = "Goodbye, friend!\n\n"
        self.assertEqual(expected_output, user_shop_choice_output)

    @patch('builtins.input', side_effect=['asdf', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_user_shop_choice_invalid_output(self, mock_output, _):
        character = {'inventory': {'gold': 100}}
        user_shop_choice(character)
        user_shop_choice_output = mock_output.getvalue()
        expected_output = "I don't know what you mean, friend. Please try again.\n\n" \
                          "Goodbye, friend!\n\n"
        self.assertEqual(expected_output, user_shop_choice_output)

    @patch('builtins.input', side_effect=['1', '3'])
    @patch('helper_functions.shop.sufficient_gold', side_effect=[None])
    def test_user_shop_choice_flux_leave(self, _, __):
        character = {'inventory': {'gold': 100}}
        self.assertEqual(None, user_shop_choice(character))

    @patch('builtins.input', side_effect=['2', '3'])
    @patch('helper_functions.shop.sufficient_gold', side_effect=[None])
    def test_user_shop_choice_repair_kit_leave(self, _, __):
        character = {'inventory': {'gold': 100}}
        self.assertEqual(None, user_shop_choice(character))

    @patch('builtins.input', side_effect=['0', '3'])
    @patch('helper_functions.shop.check_inventory', side_effect=[None])
    @patch('helper_functions.shop.sufficient_gold', side_effect=[None])
    def test_user_shop_choice_inventory_leave(self, _, __, ___):
        character = {'inventory': {'gold': 100}}
        self.assertEqual(None, user_shop_choice(character))

    def test_user_shop_choice_type_error(self):
        with self.assertRaises(TypeError):
            user_shop_choice(None)
