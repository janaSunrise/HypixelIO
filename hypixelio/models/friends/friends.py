"""This module is dedicated to definition of the Friends class."""

from .friend_data import FriendData


class Friends:
    """
    This is the definition of the Custom Hypixel API Friends Model.
    """
    def __init__(
        self,
        friends: list
    ) -> None:
        self.FRIENDS = [FriendData(friend) for friend in friends]
