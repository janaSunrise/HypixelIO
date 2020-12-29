import os
import unittest

from tests.mockdata.mock_player_data import MOCK_PLAYER

from hypixelio import Client
from hypixelio.exceptions import HypixelAPIError, PlayerNotFoundError
from hypixelio.models.player import Player


class TestPlayer(unittest.TestCase):
    """Tests for testing the player data."""
    def test_invalid_player_name(self) -> None:
        test_cases = (
            "ewdijenwmim",
            "de3in7euw9s38h23782iwksjnhuwiks"
        )

        client = Client(api_key=os.getenv("HYPIXEL_KEY"))

        for test in test_cases:
            with self.assertRaises(PlayerNotFoundError):
                client.get_player(name=test)

    def test_invalid_player_uuid(self) -> None:
        test_cases = (
            "ewdijenwmim",
            "de3in7euw9s38h23782iwksjnhuwiks"
        )

        client = Client(api_key=os.getenv("HYPIXEL_KEY"))

        for test in test_cases:
            with self.assertRaises(HypixelAPIError):
                client.get_player(uuid=test)

    def test_player_data(self) -> None:
        client = Client(api_key=os.getenv("HYPIXEL_KEY"))
        player = client.get_player(name="007rohitjj")

        self.assertIsInstance(player.HYPIXEL_ID, str)
        self.assertIsInstance(player.ACHIEVEMENT_POINTS, int)
        self.assertIsInstance(player.ONE_TIME_ACHIEVEMENTS, list)

    def test_player_first_login(self) -> None:
        data = {"firstLogin": 123456}
        player = Player(MOCK_PLAYER)
        self.assertEqual(player.FIRST_LOGIN, data["firstLogin"])

        player2 = Player(MOCK_PLAYER)
        self.assertIsInstance(player2.FIRST_LOGIN, int)

    def test_player_achievements(self) -> None:
        data = {
            "achievements": {
                'bedwars_level': 5,
                'general_challenger': 7,
                'bedwars_wins': 18,
            }
        }

        player = Player(MOCK_PLAYER)
        for key, value in player.ACHIEVEMENTS.items():
            self.assertEqual(value, data["achievements"][key])
