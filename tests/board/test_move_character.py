"""
Adam Goldsmith
A01185566
"""
from unittest import TestCase
from board import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = 'north'
        move_character(character, direction)
        self.assertEqual(0, character['Y-coordinate'])

    def test_move_character_south(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = 'south'
        move_character(character, direction)
        self.assertEqual(2, character['Y-coordinate'])

    def test_move_character_east(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = 'east'
        move_character(character, direction)
        self.assertEqual(2, character['X-coordinate'])

    def test_move_character_west(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = 'west'
        move_character(character, direction)
        self.assertEqual(0, character['X-coordinate'])

    def test_move_character_one(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = '1'
        move_character(character, direction)
        self.assertEqual(0, character['Y-coordinate'])

    def test_move_character_two(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = '2'
        move_character(character, direction)
        self.assertEqual(2, character['Y-coordinate'])

    def test_move_character_three(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = '3'
        move_character(character, direction)
        self.assertEqual(2, character['X-coordinate'])

    def test_move_character_four(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1}
        direction = '4'
        move_character(character, direction)
        self.assertEqual(0, character['X-coordinate'])
