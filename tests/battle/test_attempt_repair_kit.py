import io
from unittest import TestCase
from helper_functions.battle import attempt_repair_kit
from unittest.mock import patch

class TestAttemptRepairKit(TestCase):
    @patch('helper_functions.battle.repair_ship', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_repair_kit_insufficient_repair_kits_output(self, mock_output, _):
        character = {
            'inventory': {
                'repair_kits': 0
            }
        }
        attempt_repair_kit(character)
        attempt_repair_kit_output = mock_output.getvalue()
        expected_output = "You do not have any repair kits, captain! Please try again.\n"
        self.assertEqual(expected_output, attempt_repair_kit_output)

    @patch('helper_functions.battle.repair_ship', side_effect=[None])
    def test_attempt_repair_kit_reduce_repair_kits(self, _):
        character = {
            'inventory': {
                'repair_kits': 5
            }
        }
        attempt_repair_kit(character)
        self.assertEqual(4, character['inventory']['repair_kits'])

    def test_attempt_repair_kit_type_error(self):
        with self.assertRaises(TypeError):
            attempt_repair_kit(None, None)
