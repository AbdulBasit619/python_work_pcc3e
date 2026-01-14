import sys
from pathlib import Path

# Add Chapter 15 to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))


import matplotlib.pyplot as plt

# from random_walk import RandomWalk
from modified_random_walk import RandomWalk

# Keep making new walks as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(16, 9))
    point_numbers = range(rw.num_points)
    ax.plot(
        rw.x_values,
        rw.y_values,
        color="blue",
        linewidth=3,
    )
    ax.set_aspect("equal")

    # Emphasize the first and last points.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axis.
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.show()

    keep_running = input("Make another random walk? (y/n): ")
    if keep_running == "n":
        break
