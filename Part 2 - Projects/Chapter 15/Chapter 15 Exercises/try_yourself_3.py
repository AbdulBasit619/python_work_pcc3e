import sys
from pathlib import Path

# Add Chapter 15 to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))


import plotly.express as px

from die import Die

# # Create a D6 and a D10
# die_1 = Die(8)
# die_2 = Die(8)

# Create three D6 dies
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1_000)]
# Analyze the results.
frequencies = []
# max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
max_result = die_1.num_sides * die_2.num_sides * die_3.num_sides
poss_results = range(3, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling Three D6 Dice 1,000 Times."
labels = {"x": "Result", "y": "Frequencies of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart
fig.update_layout(xaxis_dtick=1)
fig.show()
