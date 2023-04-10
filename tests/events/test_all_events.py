from unittest import TestCase
from events import all_events
from unittest.mock import patch


class TestAllEvents(TestCase):
    @patch('events.chest', side_effect=[None])
    def test_all_events_set_chest_empty(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'chest'}
        region = []
        all_events(board, character, region)
        self.assertEqual('empty', board[(0, 0)])

    @patch('events.nymph', side_effect=[None])
    def test_all_events_set_nymph_empty(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'nymph'}
        region = []
        all_events(board, character, region)
        self.assertEqual('empty', board[(0, 0)])

    @patch('events.chest', side_effect=[None])
    def test_all_events_chest(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'chest'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.nymph', side_effect=[None])
    def test_all_events_nymph(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'nymph'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.shop', side_effect=[None])
    def test_all_events_shop(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'shop'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.boss_battle', side_effect=[None])
    def test_all_events_boss(self, _):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'boss'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[1])
    def test_all_events_battle_encounter_empty(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'empty'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[2])
    def test_all_events_battle_no_encounter_empty(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'empty'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[1])
    def test_all_events_battle_encounter_start(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'start'}
        region = []
        self.assertEqual(None, all_events(board, character, region))

    @patch('events.battle', side_effect=[None])
    @patch('random.randint', side_effect=[2])
    def test_all_events_battle_no_encounter_start(self, _, __):
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        board = {(0, 0): 'start'}
        region = []
        self.assertEqual(None, all_events(board, character, region))
