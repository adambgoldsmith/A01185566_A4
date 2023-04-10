import io
from unittest import TestCase
from helper_functions.boss import boss_battle
from unittest.mock import patch


class TestBossBattle(TestCase):
    @patch('helper_functions.boss.generate_boss', side_effect=[{'name': 'test', 'health': 0, 'attack_power': 10}])
    @patch('helper_functions.boss.boss_description', side_effect=[None])
    @patch('helper_functions.boss.boss_battle_loop', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_battle_output(self, mock_output, _, __, ___):
        character = {
            'experience': 0,
            'max_health': 100,
            'health': 100
        }
        region = ['Test Region']
        boss_battle(character, region)
        boss_battle_output = mock_output.getvalue()
        expected_output = "-------------------------\n" \
                          "test has 0 health and 10 attack power.\n" \
                          "test falls, plunging through the clouds. You have emerged victorious!\n" \
                          "You feel invigorated by your victory. You gain 100 experience points for" \
                          " conquering such a formidable foe!\n" \
                          "You continue on your journey...\n"
        self.assertEqual(expected_output, boss_battle_output)

    def test_boss_battle_type_error(self):
        with self.assertRaises(TypeError):
            boss_battle(None, None)
