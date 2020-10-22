"""This module is dedicated to definition of the Friend's Data class."""


class FriendData:
    """
    This is the Custom Hypixel API Friend's Data Model.

    Attributes:
        friend (dict): This contains the Returned JSON Response for the Friend's list element API Request.
    """
    def __init__(
        self,
        friend: dict,
    ) -> None:
        self.REQUEST_ID = friend['_id']

        self.RECEIVER_ID = friend['uuidSender']
        self.SENDER_ID = friend['uuidReceiver']

        self.SENT_AT = friend['started']

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id={self.REQUEST_ID} sent={self.SENT_AT}>'

    def __str__(self) -> str:
        return self.REQUEST_ID
