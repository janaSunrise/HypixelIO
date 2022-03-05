import typing as t

from hypixelio.utils import unix_time_to_datetime


class FriendData:
    def __init__(self, friend: dict) -> None:
        """
        Parameters
        ----------
        friend: dict
            This contains the JSON Response for the Friend's list element API Request.
        """
        self.request_id = friend["_id"]

        self.sender_id = friend["uuidSender"]
        self.receiver_id = friend["uuidReceiver"]

        self.sent_at = unix_time_to_datetime(friend["started"])

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} id="{self.request_id}" sent="{self.sent_at}">'
        )

    def __str__(self) -> str:
        return self.request_id

    def __hash__(self) -> int:
        return hash((self.sender_id, self.receiver_id))

    def __eq__(self, other: "FriendData") -> bool:
        return self.receiver_id == other.receiver_id and self.sender_id == other.sender_id


class Friends:
    def __init__(self, friends: list) -> None:
        """
        Parameters
        ----------
        friends: list
            This contains the Returned JSON Response List for the List of the friends of an user.
        """
        self.friends = [FriendData(friend) for friend in friends]

    def __len__(self) -> int:
        return len(self.friends)

    def __getitem__(self, key: int) -> FriendData:
        return self.friends[key]

    def __setitem__(self, key: int, value: FriendData) -> None:
        self.friends[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.friends)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} friends_count={len(self.friends)}>"

    def __hash__(self) -> int:
        return hash(tuple(self.friends))

    def __eq__(self, other: "Friends") -> bool:
        if len(self.friends) != len(other.friends):
            return False

        for friend in list(zip(self.friends, other.friends)):
            if friend[0].request_id != friend[1].request_id:
                return False
        return True
