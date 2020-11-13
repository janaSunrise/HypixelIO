"""This module is dedicated to definition of the Friends class."""

import collections

from .friend_data import FriendData


class Friends:
    """
    This is the Custom Hypixel API Friends Model.

    Attributes:
        friends (list):
            This contains the Returned JSON Response List for the List of the friends of an user.
    """
    def __init__(
        self,
        friends: list
    ) -> None:
        self.FRIENDS = [FriendData(friend) for friend in friends]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} friends_count={len(self.FRIENDS)}>"

    def __hash__(self) -> int:
        return hash(tuple(self.FRIENDS))

    def __eq__(self, other: "Friends") -> bool:
        if len(self.FRIENDS) != len(other.FRIENDS):
            return False

        for friend in list(zip(self.FRIENDS, other.FRIENDS)):
            if friend[0].REQUEST_ID != friend[1].REQUEST_ID:
                return False
        return True

