from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/death_valley_2021_simple.csv")

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
index_TMIN = header_row.index("TMIN")
index_TMAX = header_row.index("TMAX")

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        high = int(row[index_TMAX])
        low = int(row[index_TMIN])
    except:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


# Plot the high and low temperatures.
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.set_ylim(0, 150)
ax.tick_params(labelsize=16)

plt.show()
