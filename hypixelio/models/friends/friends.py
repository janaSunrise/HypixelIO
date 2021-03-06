import typing as t

from .friend_data import FriendData


class Friends:
    """The the Custom Hypixel API Friends Model."""
    def __init__(self, friends: list) -> None:
        """
        Parameters
        ----------
        friends: list
            This contains the Returned JSON Response List for the List of the friends of an user.
        """
        self.FRIENDS = [FriendData(friend) for friend in friends]

    def __len__(self) -> int:
        return len(self.FRIENDS)

    def __getitem__(self, key: int) -> FriendData:
        return self.FRIENDS[key]

    def __setitem__(self, key: int, value: FriendData) -> None:
        self.FRIENDS[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.FRIENDS)

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
