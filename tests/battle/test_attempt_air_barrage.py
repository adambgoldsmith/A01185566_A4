import io
from unittest import TestCase
from helper_functions.battle import attempt_air_barrage
from unittest.mock import patch


class TestAttemptAirBarrage(TestCase):
    @patch('helper_functions.battle.air_barrage', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_air_barrage_insufficient_flux_output(self, mock_output, _):
        character = {
            'inventory': {
                'flux': 0
            }
        }
        enemy = {}
        attempt_air_barrage(character, enemy)
        attempt_air_barrage_output = mock_output.getvalue()
        expected_output = "You do not have enough flux to use this ability, captain! Please try again.\n"
        self.assertEqual(expected_output, attempt_air_barrage_output)

    @patch('helper_functions.battle.air_barrage', side_effect=[None])
    def test_attempt_air_barrage_reduce_flux(self, _):
        character = {
            'inventory': {
                'flux': 10
            }
        }
        enemy = {}
        attempt_air_barrage(character, enemy)
        self.assertEqual(8, character['inventory']['flux'])

    def test_attempt_air_barrage_type_error(self):
        with self.assertRaises(TypeError):
            attempt_air_barrage(None, None)
