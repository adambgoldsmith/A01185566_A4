"""
Adam Goldsmith
A01185566
"""
import io
from unittest import TestCase
from helper_functions.boss import boss_attack
from unittest.mock import patch


class TestBossAttack(TestCase):
    @patch('random.randint', side_effect=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_attack_preparing_output(self, mock_output, _):
        character = {'health': 100}
        boss = {
            'name': 'Odeza, The Venom Wyvern',
            'attack_power': 10,
            'attack_desc': 'sweeps her tail towards you',
            'ability_power': 25,
            'prepared': False,
            'ability_desc': 'blows a huge cloud of noxious venom at you'
        }
        boss_attack(character, boss)
        boss_attack_output = mock_output.getvalue()
        expected_output = "Odeza, The Venom Wyvern gets ready to unleash a powerful attack!\n"
        self.assertEqual(expected_output, boss_attack_output)

    @patch('random.randint', side_effect=[3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_attack_prepared_output(self, mock_output, _):
        character = {'health': 100}
        boss = {
            'name': 'Odeza, The Venom Wyvern',
            'attack_power': 10,
            'attack_desc': 'sweeps her tail towards you',
            'ability_power': 25,
            'prepared': True,
            'ability_desc': 'blows a huge cloud of noxious venom at you'
        }
        boss_attack(character, boss)
        boss_attack_output = mock_output.getvalue()
        expected_output = "Odeza, The Venom Wyvern has unleashed a powerful attack!\n" \
                          "Odeza, The Venom Wyvern blows a huge cloud of noxious venom at you." \
                          " It dealt 25 damage! You have 75 health remaining.\n"
        self.assertEqual(expected_output, boss_attack_output)

    @patch('random.randint', side_effect=[2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_attack_regular_attack_output(self, mock_output, _):
        character = {'health': 100}
        boss = {
            'name': 'Odeza, The Venom Wyvern',
            'attack_power': 10,
            'attack_desc': 'sweeps her tail towards you',
            'ability_power': 25,
            'prepared': False,
            'ability_desc': 'blows a huge cloud of noxious venom at you'
        }
        boss_attack(character, boss)
        boss_attack_output = mock_output.getvalue()
        expected_output = "Odeza, The Venom Wyvern sweeps her tail towards you. It dealt 10 damage!" \
                          " You have 90 health remaining.\n"
        self.assertEqual(expected_output, boss_attack_output)

    @patch('random.randint', side_effect=[3])
    def test_boss_attack_prepared_damage(self, _):
        character = {'health': 100}
        boss = {
            'name': 'Odeza, The Venom Wyvern',
            'attack_power': 10,
            'attack_desc': 'sweeps her tail towards you',
            'ability_power': 25,
            'prepared': True,
            'ability_desc': 'blows a huge cloud of noxious venom at you'
        }
        boss_attack(character, boss)
        self.assertEqual(75, character['health'])

    @patch('random.randint', side_effect=[2])
    def test_boss_attack_regular_attack_damage(self, _):
        character = {'health': 100}
        boss = {
            'name': 'Odeza, The Venom Wyvern',
            'attack_power': 10,
            'attack_desc': 'sweeps her tail towards you',
            'ability_power': 25,
            'prepared': False,
            'ability_desc': 'blows a huge cloud of noxious venom at you'
        }
        boss_attack(character, boss)
        self.assertEqual(90, character['health'])

    def test_boss_attack_type_error(self):
        with self.assertRaises(TypeError):
            boss_attack(None, None)
