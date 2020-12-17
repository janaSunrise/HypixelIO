import os
import unittest

from pytest_benchmark.plugin import benchmark

from hypixelio import Client
from hypixelio.exceptions import HypixelAPIError, PlayerNotFoundError


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
