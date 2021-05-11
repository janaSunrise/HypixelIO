import unittest

from hypixelio import Converters as Conv


class TestUsernameToUUID(unittest.TestCase):
    """Test for the Username to UUID conversion."""

    def test_conversion(self) -> None:
        test_cases = (
            ("janaSunrise", "c8438cdd126043448cca9e28646efbe7"),
            ("JanaSunrise123", "b4ead04f4e2d484ba70257d5729aa773"),
            ("007rohitjj", "2a13b3a34bf343fa9d8db0f87187da39"),
        )

        for username, uuid in test_cases:
            self.assertEqual(Conv.username_to_uuid(username), uuid)


class TestUUIDToUsername(unittest.TestCase):
    """Test for the UUID to Username conversion."""

    def test_conversion(self) -> None:
        test_cases = (
            ("janaSunrise", "c8438cdd126043448cca9e28646efbe7"),
            ("JanaSunrise123", "b4ead04f4e2d484ba70257d5729aa773"),
            ("007rohitjj", "2a13b3a34bf343fa9d8db0f87187da39"),
        )

        for username, uuid in test_cases:
            self.assertEqual(username, Conv.uuid_to_username(uuid))
