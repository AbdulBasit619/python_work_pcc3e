from pathlib import Path
import csv

import plotly.express as px

# # Read data as a string and convert to a Python object.
# # path = Path("eq_data/eq_data_30_day_m1.geojson")

# # For task 16-8
# path = Path("Chapter 16 Exercises/eq_data/eq_data_7_day_m1.geojson")
# contents = path.read_text(encoding="utf-8")
# all_eq_data = json.loads(contents)

# # # Create a more readable version of the data file.
# path = Path("Chapter 16 Exercises/eq_data/readable_eq_data_7_day.geojson")
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# # Examine all earthquakes in a dataset.
# all_eq_dicts = all_eq_data["features"]

# mags, lons, lats, eq_titles = [], [], [], []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict["properties"]["mag"]
#     mags.append(abs(mag))
#     lons.append(eq_dict["geometry"]["coordinates"][0])
#     lats.append(eq_dict["geometry"]["coordinates"][1])
#     eq_titles.append(eq_dict["properties"]["title"])

# title = all_eq_data["metadata"]["title"]
# fig = px.scatter_geo(
#     lat=lats,
#     lon=lons,
#     size=mags,
#     color=mags,
#     color_continuous_scale="viridis",
#     labels={"color": "Magnitude"},
#     projection="natural earth",
#     title=title,
#     hover_name=eq_titles,
# )
# fig.show()

path = Path("Chapter 16 Exercises/world_fires_1_day.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

index_lon = header_row.index("longitude")
index_lat = header_row.index("latitude")
index_brght = header_row.index("brightness")

lons, lats, brghts = [], [], []
for row in reader:
    lon = row[index_lon]
    lat = row[index_lat]
    brght = row[index_brght]
    lons.append(lon)
    lats.append(lat)
    brghts.append(brght)

# Plot the map
title = "World Fires"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    color=brghts,
    color_continuous_scale="hot",
    labels={"color": "Fire Intensity"},
    title=title,
    projection="natural earth",
    hover_name=brghts,
)

fig.show()
