import os
from textwrap import dedent

import hypixelio as hp

# Init the Client
client = hp.Client(api_key=os.environ["HYPIXEL_KEY"])

# Get the watchdog stats
watchdog = client.get_watchdog_info()

# Extract the Data
last_minute_ban = watchdog.LAST_MINUTE_BAN
total_bans = watchdog.TOTAL_BANS
rolling_daily = watchdog.ROLLING_DAILY

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
