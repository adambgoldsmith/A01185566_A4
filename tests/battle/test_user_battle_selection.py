"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from battle import user_battle_selection
from unittest.mock import patch


class TestUserBattleSelection(TestCase):
    @patch('builtins.input', side_effect=['0', '1'])
    def test_user_battle_selection_zero_other(self, _):
        character = {
            'X-coordinate': 0,
            'Y-coordinate': 0,
            'name': 'Captain Magnus Selwood',  # unused, but interesting lore
            'level': 1,
            'experience': 0,
            'max_health': 100,
            'health': 100,
            'attack_power': 10,
            'ability_power': 20,
            'inventory': {
                'flux': 10,
                'repair_kits': 1,
                'gold': 0,
            },
        }
        enemy = {
            'type': 'regular',
            'name': 'the pirate ship',
            'health': 50,
            'attack_power': 10,
        }
        self.assertEqual(False, user_battle_selection(character, enemy))
