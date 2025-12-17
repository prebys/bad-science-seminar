import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Use notebook-friendly animation display
#from IPython.display import HTML

# Parameters
n_bins = 20
samples_per_frame = 1
frames = 1000

# Create figure and axis
fig, ax = plt.subplots()
#counts, bins, patches = ax.hist([], bins=n_bins, range=(-5, 5), color="skyblue", edgecolor="black")
#ax.set_xlim(-5, 5)
#ax.set_ylim(0, 50)
#ax.set_xlabel("Value")
#ax.set_ylabel("Count")
#ax.set_title("Animated Histogram Filling")

# Data storage
all_data = []
ymax = 10
def update(frame):
    global all_data
    global ymax
    # Add new random samples
    new_data = np.random.normal(loc=0, scale=1, size=samples_per_frame)
    all_data.extend(new_data)
    # Clear and re-draw histogram
    ax.cla()
    counts,bins,patches = ax.hist(all_data, bins=n_bins, range=(-5, 5), color="skyblue", edgecolor="black")
    ax.set_xlim(-5, 5)
    if np.array(counts).max() > ymax:
        ymax *= 2
    ax.set_ylim(0, ymax)
    ax.set_title(f"Frame {frame+1}")
    ax.set_xlabel("Value")
    ax.grid()
    ax.set_ylabel("Count")

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=100, repeat=False)

# Display in notebook
#HTML(ani.to_jshtml())

plt.show()
