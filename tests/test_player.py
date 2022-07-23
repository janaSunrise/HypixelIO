import os
import unittest
from typing import cast

from hypixelio import Client
from hypixelio.exceptions import HypixelAPIError, PlayerNotFoundError
from hypixelio.models.player import Player
from tests.mock_data.player_data import PLAYER_MOCK

API_KEY = cast(str, os.getenv("HYPIXEL_KEY"))

if not API_KEY:
    raise Exception("Please set the HYPIXEL_KEY environment variable.")


class TestPlayer(unittest.TestCase):
    """Tests for testing the player data."""

    def test_invalid_player_name(self) -> None:
        test_cases = ("ewdijenwmim", "de3in7euw9s38h23782iwksjnhuwiks")

        client = Client(api_key=API_KEY)

        for test in test_cases:
            with self.assertRaises(PlayerNotFoundError):
                client.get_player(name=test)

    def test_invalid_player_uuid(self) -> None:
        test_cases = ("ewdijenwmim", "de3in7euw9s38h23782iwksjnhuwiks")

        client = Client(api_key=API_KEY)

        for test in test_cases:
            with self.assertRaises(HypixelAPIError):
                client.get_player(uuid=test)

    def test_player_data(self) -> None:
        client = Client(api_key=API_KEY)
        player = client.get_player(name="VSCode_")

        self.assertIsInstance(player.hypixel_id, str)
        self.assertIsInstance(player.achievement_points, int)
        self.assertIsInstance(player.one_time_achievements, list)

    def test_player_achievements(self) -> None:
        data = {
            "achievements": {
                "bedwars_level": 5,
                "general_challenger": 7,
                "bedwars_wins": 18,
            }
        }

        player = Player(PLAYER_MOCK)
        for key, value in player.achievements.items():
            self.assertEqual(value, data["achievements"][key])
