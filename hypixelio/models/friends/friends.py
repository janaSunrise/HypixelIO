"""This module is dedicated to definition of the Friends class."""

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
