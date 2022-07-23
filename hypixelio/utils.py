import math
import re
import typing as t
from datetime import datetime

from .constants import RANKS, RANK_COLORS


# Form URL
def form_url(main_url: str, url: str, data: t.Optional[t.Dict[str, t.Any]] = None) -> str:
    if not data:
        data = {}

    url = main_url + url if url.startswith("/") else url
    url += "?" + "&".join([f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()])

    return url


# Convert unix time to datetime
def unix_time_to_datetime(unix_time: int) -> datetime:
    return datetime.fromtimestamp(float(unix_time) / 1000)


# Other useful functions
def get_ratio(
    positive_stat: t.Union[int, float], negative_stat: t.Union[int, float]
) -> t.Union[int, float]:
    try:
        ratio = positive_stat / negative_stat
        return round(ratio, 2)
    except ZeroDivisionError:
        return float("inf") if positive_stat > 0 else 0


def get_ratio_next(ratio: t.Union[int, float]) -> t.Union[int, float]:
    if ratio == float("inf"):
        return ratio
    return math.trunc(ratio) + 1


def get_level_percentage(level: float) -> t.Union[int, float]:
    return round((level - math.trunc(level)) * 100, 2)


def get_network_level(experience: t.Union[int, float]) -> t.Union[int, float]:
    return math.trunc(get_network_level_exact(experience))


def get_network_level_exact(experience: t.Union[int, float]) -> t.Union[int, float]:
    return (math.sqrt(experience + 15312.5) - 88.38834764831843) / 35.35533905932738


def get_rank(
    rank: t.Optional[str] = None,
    prefix_raw: t.Optional[str] = None,
    monthly_package_rank: t.Optional[str] = None,
    new_package_rank: t.Optional[str] = None,
    package_rank: t.Optional[str] = None,
) -> t.Optional[str]:
    real_rank = None

    if prefix_raw:
        prefix = re.sub(r"§.", "", prefix_raw)[1:-1]
        real_rank = RANKS.get(prefix, prefix)
    elif rank and rank != "NORMAL" and not real_rank:
        real_rank = RANKS.get(rank, rank)
    elif new_package_rank and not real_rank:
        real_rank = RANKS.get(new_package_rank, new_package_rank)
    elif package_rank and not real_rank:
        real_rank = RANKS.get(package_rank, package_rank)
    elif (monthly_package_rank and monthly_package_rank != "NONE") and not real_rank:
        real_rank = RANKS.get(monthly_package_rank, monthly_package_rank)

    return real_rank


def get_rank_color(rank: str) -> int:
    return RANK_COLORS[rank]
