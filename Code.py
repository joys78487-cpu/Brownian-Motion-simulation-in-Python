import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# PARAMETERS
N = 200                 # fewer particles (simpler)
box_size = 10
dt = 0.05
temperature = 1        # change this value to see effect

# INITIAL POSITIONS
positions = np.random.rand(N, 2) * box_size

# VELOCITIES depend on temperature
velocities = np.random.randn(N, 2) * np.sqrt(temperature)

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_title("Brownian Motion Simulation")

scatter = ax.scatter(positions[:,0], positions[:,1], s=20)

def update(frame):
    global positions, velocities
    
    positions += velocities * dt

    # Wall collision
    for i in range(N):
        for d in range(2):
            if positions[i, d] <= 0 or positions[i, d] >= box_size:
                velocities[i, d] *= -1

    speeds = np.linalg.norm(velocities, axis=1)

    # Normalize for color mapping
    norm = (speeds - speeds.min()) / (speeds.max() - speeds.min() + 1e-5)
    colors = sns.color_palette("coolwarm", as_cmap=True)(norm)

    scatter.set_offsets(positions)
    scatter.set_color(colors)

    return scatter,

ani = FuncAnimation(fig, update, frames=400, interval=30)
ani.save("simulation.gif", writer="pillow")

plt.show()
