#IS THIS FILE WORKING

import matplotlib.pyplot as plt

#Non-Bézier solution:
#Create a downwards-opening quadratic curve, with one end at (0,0) and the other end at (1,0), so that the vertex is (0.5, f(0.5)). 

from Bezier import Bezier
import numpy as np

t_points = np.arange(0, 1, 0.01) #................................. Creates an iterable list from 0 to 1.
points1 = np.array([[0, 0], [3, 4], [7, 4], [10, 0]]) #.... Creates an array of coordinates.
curve1 = Bezier.Curve(t_points, points1) #......................... Returns an array of coordinates.

plt.figure()
plt.plot(
	curve1[:, 0],   # x-coordinates.
	curve1[:, 1]    # y-coordinates.
)
plt.plot(
	points1[:, 0],  # x-coordinates.
	points1[:, 1],  # y-coordinates.
	'ro:'           # Styling (red, circles, dotted).
)
plt.grid()
plt.show()
