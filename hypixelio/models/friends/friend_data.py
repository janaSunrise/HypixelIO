class FriendData:
    """
    This is the Custom Hypixel API Friend's Data Model.
    """
    def __init__(self, friend: dict) -> None:
        """
        Parameters
        ----------
        friend: dict
            This contains the JSON Response for the Friend's list element API Request.
        """
        self.REQUEST_ID = friend['_id']

        self.RECEIVER_ID = friend['uuidSender']
        self.SENDER_ID = friend['uuidReceiver']

        self.SENT_AT = friend['started']

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.REQUEST_ID}" sent="{self.SENT_AT}">'

    def __str__(self) -> str:
        return self.REQUEST_ID

    def __hash__(self) -> int:
        return hash((self.RECEIVER_ID, self.SENDER_ID))

    def __eq__(self, other: "FriendData") -> bool:
        return self.RECEIVER_ID == other.RECEIVER_ID and self.SENDER_ID == other.SENDER_ID
