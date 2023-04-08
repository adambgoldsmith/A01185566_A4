import io
from unittest import TestCase
from chest import chest
from unittest.mock import patch


class TestChest(TestCase):
    @patch('chest.generate_puzzle', side_effect=['I'])
    @patch('chest.user_puzzle_choice', side_effect=['I'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chest_correct_output(self, mock_output, _, __):
        character = {'inventory': {
            'gold': 0
        }}
        chest(character)
        chest_output = mock_output.getvalue()
        expected_output = "-------------------------\n"\
                          "Out of the corner of your eye you spot a shimmering chest on a tiny floating island.\n"\
                          "You approach the chest and notice several gemstones of differing shapes above the heavy" \
                          " iron latch.\n"\
                          "You hear a loud click. The chest swings open to reveal 50 gold coins!" \
                          " You collect your spoils and head back to your ship.\n"
        self.assertEqual(expected_output, chest_output)

    @patch('chest.generate_puzzle', side_effect=['I'])
    @patch('chest.user_puzzle_choice', side_effect=['O'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_chest_incorrect_output(self, mock_output, _, __):
        character = {'inventory': {
            'gold': 0
        }}
        chest(character)
        chest_output = mock_output.getvalue()
        expected_output = "-------------------------\n"\
                          "Out of the corner of your eye you spot a shimmering chest on a tiny floating island.\n"\
                          "You approach the chest and notice several gemstones of differing shapes above the heavy" \
                          " iron latch.\n"\
                          "That doesn't look right. The gemstones fade of their"\
                          " colours. You head back to your ship empty handed...\n"
        self.assertEqual(expected_output, chest_output)

    @patch('chest.generate_puzzle', side_effect=['I'])
    @patch('chest.user_puzzle_choice', side_effect=['I'])
    def test_chest_correct_answer(self, _, __):
        character = {'inventory': {
            'gold': 0
        }}
        chest(character)
        self.assertEqual(50, character['inventory']['gold'])

    @patch('chest.generate_puzzle', side_effect=['V'])
    @patch('chest.user_puzzle_choice', side_effect=['X'])
    def test_chest_incorrect_answer(self, _, __):
        character = {'inventory': {
            'gold': 0
        }}
        chest(character)
        self.assertEqual(0, character['inventory']['gold'])
