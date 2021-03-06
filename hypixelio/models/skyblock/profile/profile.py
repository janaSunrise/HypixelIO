import typing as t

from .profile_member import SkyblockProfileMember


class SkyblockProfile:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.__PROFILE_JSON = data["profile"]

        self.PROFILE_ID = self.__PROFILE_JSON["profile_id"]
        self.MEMBERS = [
            SkyblockProfileMember(self.__PROFILE_JSON["members"][member]) for member in self.__PROFILE_JSON["members"]
        ]
        self.COMMUNITY_UPGRADES = self.__PROFILE_JSON["community_upgrades"]

    def __str__(self) -> str:
        return self.PROFILE_ID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.PROFILE_ID}" member_count="{len(self.MEMBERS)}">'

    def __hash__(self) -> int:
        return hash(self.PROFILE_ID)

    def __eq__(self, other: "SkyblockProfile") -> bool:
        return self.PROFILE_ID == other.PROFILE_ID

    def __len__(self) -> int:
        return len(self.MEMBERS)

    def __getitem__(self, key: int) -> SkyblockProfileMember:
        return self.MEMBERS[key]

    def __setitem__(self, key: int, value: SkyblockProfileMember) -> None:
        self.MEMBERS[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.MEMBERS)
