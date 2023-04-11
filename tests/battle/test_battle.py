import io
from unittest import TestCase
from helper_functions.battle import battle
from unittest.mock import patch


class TestBattle(TestCase):
    @patch('helper_functions.battle.generate_enemy_ship', side_effect=[{'health': 100, 'attack_power': 10}])
    @patch('helper_functions.battle.battle_loop', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_enemy_alive_output(self, mock_output, _, __):
        character = {
            'experience': 0,
            'inventory': {
                'gold': 0
            }
        }
        battle(character)
        battle_output = mock_output.getvalue()
        expected_output = "-------------------------\n" \
                          "You spot a hostile air ship on the horizon. As the ship gets closer, your eyes are" \
                          " drawn to the large skull\n" \
                          "and crossbones crudely painted on it's side. Pirates! You ready your cannons for battle.\n" \
                          "The enemy ship has 100 health and 10 attack power.\n"
        self.assertEqual(expected_output, battle_output)

    @patch('helper_functions.battle.generate_enemy_ship', side_effect=[{'health': 0, 'attack_power': 10}])
    @patch('helper_functions.battle.battle_loop', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_enemy_dead_output(self, mock_output, _, __):
        character = {
            'experience': 0,
            'inventory': {
                'gold': 0
            }
        }
        battle(character)
        battle_output = mock_output.getvalue()
        expected_output = "-------------------------\n" \
                          "You spot a hostile air ship on the horizon. As the ship gets closer, your eyes are" \
                          " drawn to the large skull\n" \
                          "and crossbones crudely painted on it's side. Pirates! You ready your cannons for battle.\n" \
                          "The enemy ship has 0 health and 10 attack power.\n" \
                          "The hostile ship plummets through the clouds and explodes in a fiery ball" \
                          " of flames. Well done, captain! You stand victorious!\n" \
                          "You gain 50 gold coins for your victory.\n" \
                          "You gain 25 experience points for your victory.\n"
        self.assertEqual(expected_output, battle_output)

    @patch('helper_functions.battle.generate_enemy_ship', side_effect=[{'health': 0, 'attack_power': 10}])
    @patch('helper_functions.battle.battle_loop', side_effect=[None])
    def test_battle_increase_experience(self, _, __):
        character = {
            'experience': 0,
            'inventory': {
                'gold': 0
            }
        }
        battle(character)
        self.assertEqual(25, character['experience'])

    @patch('helper_functions.battle.generate_enemy_ship', side_effect=[{'health': 0, 'attack_power': 10}])
    @patch('helper_functions.battle.battle_loop', side_effect=[None])
    def test_battle_increase_experience(self, _, __):
        character = {
            'experience': 0,
            'inventory': {
                'gold': 0
            }
        }
        battle(character)
        self.assertEqual(50, character['inventory']['gold'])

    def test_battle_type_error(self):
        with self.assertRaises(TypeError):
            battle(None)
