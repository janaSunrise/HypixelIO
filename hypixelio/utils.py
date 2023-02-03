import math
import re
from datetime import datetime
from typing import Any, Dict, Optional, Union

from .constants import RANKS, RANK_COLORS


def form_url(main_url: str, url: str, data: Optional[Dict[str, Any]] = None) -> str:
    if not data:
        data = {}

    url = main_url + url if url.startswith("/") else url
    url += "?" + "&".join(
        [f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()]
    )

    return url


# Convert unix time to datetime
def unix_time_to_datetime(unix_time: int) -> datetime:
    return datetime.fromtimestamp(float(unix_time) / 1000)


# Other useful functions
def get_ratio(
    positive_stat: Union[int, float], negative_stat: Union[int, float]
) -> Union[int, float]:
    try:
        ratio = positive_stat / negative_stat
        return round(ratio, 2)
    except ZeroDivisionError:
        return float("inf") if positive_stat > 0 else 0


def get_ratio_next(ratio: Union[int, float]) -> Union[int, float]:
    if ratio == float("inf"):
        return ratio
    return math.trunc(ratio) + 1


def get_level_percentage(level: float) -> Union[int, float]:
    return round((level - math.trunc(level)) * 100, 2)


def get_network_level(experience: Union[int, float]) -> Union[int, float]:
    return math.trunc(get_network_level_exact(experience))


def get_network_level_exact(experience: Union[int, float]) -> Union[int, float]:
    return (math.sqrt(experience + 15312.5) - 88.38834764831843) / 35.35533905932738


def get_rank(
    rank: Optional[str] = None,
    prefix_raw: Optional[str] = None,
    monthly_package_rank: Optional[str] = None,
    new_package_rank: Optional[str] = None,
    package_rank: Optional[str] = None,
) -> Optional[str]:
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
