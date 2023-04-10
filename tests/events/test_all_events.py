from unittest import TestCase
from helper_functions.events import all_events
from unittest.mock import patch


class TestAllEvents(TestCase):
    @patch('helper_functions.events.chest', side_effect=[None])
    def test_all_events_set_chest_empty(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'chest'}
        region = []
        all_events(board, character, region)
        self.assertEqual('empty', board[(0, 0)])

    @patch('helper_functions.events.nymph', side_effect=[None])
    def test_all_events_set_nymph_empty(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'nymph'}
        region = []
        all_events(board, character, region)
        self.assertEqual('empty', board[(0, 0)])

    @patch('helper_functions.events.chest', side_effect=[None])
    def test_all_events_chest(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'chest'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.nymph', side_effect=[None])
    def test_all_events_nymph(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'nymph'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.shop', side_effect=[None])
    def test_all_events_shop(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'shop'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.boss_battle', side_effect=[None])
    def test_all_events_boss(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'boss'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[1])
    def test_all_events_battle_encounter_empty(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'empty'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[2])
    def test_all_events_battle_no_encounter_empty(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'empty'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[1])
    def test_all_events_battle_encounter_start(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'start'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('helper_functions.events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[2])
    def test_all_events_battle_no_encounter_start(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'start'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    def test_all_events_type_error(self):
        with self.assertRaises(TypeError):
            all_events(None, None, None)

    def test_all_events_key_error(self):
        with self.assertRaises(KeyError):
            character = {'X-coordinate': 0, 'Y-coordinate': 0}
            board = {(-1, 0): 'start'}
            region = []
            all_events(board, character, region)
