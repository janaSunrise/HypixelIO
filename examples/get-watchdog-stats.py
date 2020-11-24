from textwrap import dedent

import hypixelio as hp

# Init the Client
client = hp.Client(api_key="your-api-key")

# Get the watchdog stats
watchdog = client.get_watchdog_info()

# Extract the Data
last_minute_ban = watchdog.LAST_MINUTE_BAN
total_bans = watchdog.TOTAL_BANS
rolling_daily = watchdog.WATCHDOG_ROLLING_DAILY

# Display the data
print(
    dedent(f"""
    Last minute ban: {last_minute_ban}
    Total Bans: {total_bans}
    Rolling daily: {rolling_daily}
    """)
)
