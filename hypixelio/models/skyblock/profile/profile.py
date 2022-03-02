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
        self.__profile_json = data["profile"]

        self.profile_id = self.__profile_json["profile_id"]
        self.members = [
            SkyblockProfileMember(self.__profile_json["members"][member])
            for member in self.__profile_json["members"]
        ]
        self.community_upgrades = self.__profile_json["community_upgrades"]

    def __str__(self) -> str:
        return self.profile_id

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.profile_id}" member_count="{len(self.members)}">'

    def __hash__(self) -> int:
        return hash(self.profile_id)

    def __eq__(self, other: "SkyblockProfile") -> bool:
        return self.profile_id == other.profile_id

    def __len__(self) -> int:
        return len(self.members)

    def __getitem__(self, key: int) -> SkyblockProfileMember:
        return self.members[key]

    def __setitem__(self, key: int, value: SkyblockProfileMember) -> None:
        self.members[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.members)
