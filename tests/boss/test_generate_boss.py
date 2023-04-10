"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from helper_functions.boss import generate_boss


class TestGenerateBoss(TestCase):
    def test_generate_boss_one(self):
        region = ['The Cloud Expanse']
        self.assertEqual({
            'type': 'boss',
            'name': 'Odeza, The Venom Wyvern',
            'health': 150,
            'attack_power': 10,
            'attack_desc': 'sweeps her tail towards you',
            'ability_power': 25,
            'prepared': False,
            'ability_desc': 'blows a huge cloud of noxious venom at you'},
            generate_boss(region))

    def test_generate_boss_two(self):
        region = ['Fogmourne']
        self.assertEqual({
            'type': 'boss',
            'name': 'Nebulous, The Mist Colossus',
            'health': 250,
            'attack_power': 15,
            'attack_desc': 'swings his colossal mace at you',
            'ability_power': 30,
            'prepared': False,
            'ability_desc': 'raises his mace high above his head and brings it down with a thunderous crash'},
            generate_boss(region))

    def test_generate_boss_three(self):
        region = ['The Void Isles']
        self.assertEqual({
            'type': 'boss',
            'name': 'FOLGRIM, The Void Kraken',
            'health': 500,
            'attack_power': 35,
            'attack_desc': 'grapples its tentacles around your ship and squeezes tight',
            'ability_power': 50,
            'prepared': False,
            'ability_desc': 'opens its maw and unleashes a torrent of void energy'},
            generate_boss(region))

    def test_generate_boss_type_error(self):
        with self.assertRaises(TypeError):
            generate_boss(None)

    def test_generate_boss_value_error(self):
        with self.assertRaises(ValueError):
            generate_boss(['invalid region'])
