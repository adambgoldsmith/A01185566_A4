import io
from unittest import TestCase
from character import check_inventory
from unittest.mock import patch


class TestCheckInventory(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_inventory(self, mock_output):
        character = {
            'inventory': {
                'gold': 100,
                'flux': 10,
                'repair_kits': 1
            }
        }
        check_inventory(character)
        check_inventory_output = mock_output.getvalue()
        expected_output = "Flux: 10\n" \
                          "Repair Kits: 1\n" \
                          "Gold: 100\n\n"
        self.assertEqual(expected_output, check_inventory_output)
