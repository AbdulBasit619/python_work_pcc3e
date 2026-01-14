from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# # Weather data for Sitka
# # path = Path("Chapter 16 Exercises\weather_data\sitka_weather_2021_full.csv")
# # Weather data for Death Valley
# path = Path("Chapter 16 Exercises\weather_data\death_valley_2021_full.csv")

# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # Plot the Rainfall chance (PRCP)
# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# # Extract datetime and PRCP from dataset.
# dates, precipitations = [], []
# for row in reader:
#     current_date = datetime.strptime(row[2], "%Y-%m-%d")
#     try:
#         precipitation = float(row[5])
#     except:
#         print(f"Missing data for {current_date}")
#     else:
#         precipitations.append(precipitation)
#     dates.append(current_date)

# # Plot the rainfall
# fig, ax = plt.subplots()
# ax.plot(dates, precipitations, color="blue")

# # Format the plot.
# # ax.set_title("Daily Rainfall in Sitka, 2021", fontsize=24)
# ax.set_title("Daily Rainfall in Death Valley, 2021", fontsize=24)
# fig.autofmt_xdate()
# ax.set_xlabel("", fontsize=16)
# ax.set_ylabel("Chance of Rainfall (%)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()


# Weather data for Sitka
path = Path("Chapter 16 Exercises\weather_data\san_francisco_weather_2025_simple.csv")

lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates and high and low temperatures from dataset.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[header_row.index("DATE")], "%Y-%m-%d")
    try:
        high = float(row[header_row.index("TMAX")])
        low = float(row[header_row.index("TMIN")])
    except:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# Plot the temperatures
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)

# Format the plot.
ax.set_title("Daily Temperature in San Francisco, 2025", fontsize=24)
fig.autofmt_xdate()
ax.fill_between(dates, highs, lows, color="green", alpha=0.1)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Daily Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# # Weather data for Sitka
# path = Path("Chapter 16 Exercises\weather_data\sitka_weather_2021_full.csv")

# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)

# # Plot the daily 2-min average wind speed (WSF2)
# # for index, column_header in enumerate(header_row):
# #     print(index, column_header)

# # Extract datetime and WSF2 from dataset.
# dates, two_min_wind_speeds = [], []
# for row in reader:
#     current_date = datetime.strptime(row[header_row.index("DATE")], "%Y-%m-%d")
#     try:
#         wind_speed = float(row[header_row.index("WSF2")])
#     except:
#         print(f"Missing data for {current_date}")
#     else:
#         two_min_wind_speeds.append(wind_speed)
#         dates.append(current_date)

# # Plot the rainfall
# fig, ax = plt.subplots()
# ax.plot(dates, two_min_wind_speeds, color="blue")

# # Format the plot.
# ax.set_title("Average 2-min Wind Speeds in Sitka, 2021", fontsize=24)
# fig.autofmt_xdate()
# ax.set_xlabel("", fontsize=16)
# ax.set_ylabel("Average Wind Speed (mph)", fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()
