import matplotlib.pyplot as plt

## Plot first 5 numbers.
# x_values = [1, 2, 3, 4, 5]

## Plot first 5000 numbers
x_values = range(1, 5001)

y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
# Plot a simple line plot
# ax.plot(x_values, y_values, linewidth=2)

# Plot a scatter plot with color maps
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)


# Set the title and labels
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)

ax.tick_params(labelsize=14)
ax.axis([0, 5_100, 0, 132_652_000_000])

plt.show()
