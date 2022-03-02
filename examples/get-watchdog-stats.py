import os
from textwrap import dedent

import hypixelio as hp

# Init the Client
client = hp.Client(api_key=os.environ["HYPIXEL_KEY"])

# Get the watchdog stats
watchdog = client.get_watchdog_info()

# Extract the Data
last_minute_ban = watchdog.last_minute_ban
total_bans = watchdog.total_bans
rolling_daily = watchdog.rolling_daily

# Display the data
print(
    dedent(
        f"""
    Last minute ban: {last_minute_ban}
    Total Bans: {total_bans}
    Rolling daily: {rolling_daily}
    """
    )
)
