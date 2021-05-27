from datetime import datetime


def unix_time_to_datetime(unix_time: int) -> datetime:
    return datetime.fromtimestamp(float(unix_time) / 1000)
