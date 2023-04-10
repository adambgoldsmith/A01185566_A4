"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.character import create_character


class TestCreateCharacter(TestCase):
    def test_create_character(self):
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
        self.assertEqual(character, create_character())

    def test_create_character_length(self):
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
        self.assertEqual(10, len(character))

    def test_create_character_inventory_length(self):
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
        self.assertEqual(3, len(character['inventory']))

    def test_create_character_x_coordinate(self):
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
        self.assertEqual(0, character['X-coordinate'])

    def test_create_character_y_coordinate(self):
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
        self.assertEqual(0, character['Y-coordinate'])

    def test_create_character_name(self):
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
        self.assertEqual('Captain Magnus Selwood', character['name'])

    def test_create_character_level(self):
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
        self.assertEqual(1, character['level'])

    def test_create_character_experience(self):
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
        self.assertEqual(0, character['experience'])

    def test_create_character_max_health(self):
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
        self.assertEqual(100, character['max_health'])

    def test_create_character_health(self):
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
        self.assertEqual(100, character['health'])

    def test_create_character_attack_power(self):
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
        self.assertEqual(10, character['attack_power'])

    def test_create_character_ability_power(self):
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
        self.assertEqual(20, character['ability_power'])

    def test_create_character_inventory(self):
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
        self.assertEqual({'flux': 10,
                          'repair_kits': 1,
                          'gold': 0}, character['inventory'])
