import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, Rectangle
import matplotlib.pyplot as plt

# Create figure and axes
fig, ax = plt.subplots()

plt.plot(10, 10)

# Create a Rectangle patch
rect = Rectangle((0.2, 0.2), 0.5, 0.5, linewidth=1,
                 edgecolor='r', facecolor='none')

circle1 = plt.Circle((10, 10), 2, color='r')

# Add the patch to the Axes
ax.add_patch(rect)
ax.add_patch(circle1)

plt.show()
