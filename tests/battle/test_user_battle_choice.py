"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.battle import get_user_battle_choice
from unittest.mock import patch


class TestUserBattleChoice(TestCase):
    @patch('builtins.input', side_effect=['invalid', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_battle_choice_invalid_one_output(self, mock_output, _):
        enemy = {'attack_power': 10}
        get_user_battle_choice(enemy)
        get_user_battle_choice_output = mock_output.getvalue()
        expected_output = "I don't understand your order, captain! Please try again.\n"
        self.assertEqual(expected_output, get_user_battle_choice_output)

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_battle_choice_one(self, _):
        enemy = {'attack_power': 10}
        self.assertEqual('1', get_user_battle_choice(enemy))

    @patch('builtins.input', side_effect=['2'])
    def test_get_user_battle_choice_two(self, _):
        enemy = {'attack_power': 10}
        self.assertEqual('2', get_user_battle_choice(enemy))

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_battle_choice_three(self, _):
        enemy = {'attack_power': 10}
        self.assertEqual('3', get_user_battle_choice(enemy))

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_battle_choice_four(self, _):
        enemy = {'attack_power': 10}
        self.assertEqual('4', get_user_battle_choice(enemy))

    @patch('builtins.input', side_effect=['0'])
    def test_get_user_battle_choice_zero(self, _):
        enemy = {'attack_power': 10}
        self.assertEqual('0', get_user_battle_choice(enemy))

    def test_get_user_battle_choice_type_error(self):
        with self.assertRaises(TypeError):
            get_user_battle_choice(None)
