from unittest import TestCase
from helper_functions.battle import generate_enemy_ship


class TestGenerateEnemyShip(TestCase):
    def test_generate_enemy_ship(self):
        self.assertEqual({'attack_power': 10, 'health': 50, 'name': 'the pirate ship', 'type': 'regular'},
                         generate_enemy_ship())
