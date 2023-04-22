import matplotlib.pyplot as plt
import numpy as np
from math import *
# x_data = [.1, .2, .3, .4, .5]
# y_data = [.10, .5, .7, .12, .8]

x_points = []
y_points = []

with open("fractalList.txt", "r") as f:
    lines = f.readlines()
    # necessaryLines = lines[1:31410]
    necessaryLines = lines[31411:]
    print(necessaryLines[0])
    print(necessaryLines[-1])
    for l in necessaryLines:
        x, y = l.split(", ")
        x_points.append(float(x) + 0.000001)
        y_points.append(float(y) + 0.000001)
fig, ax = plt.subplots()

#gridline space = 0.01
# for i in range(-141, 141):
#     x_pos = i * 0.01
#     ax.axvline(x=x_pos, color='red', linestyle='-', linewidth=0.8)
# for i in range(-141, 141):
#     y_pos = i * 0.01
#     ax.axhline(y=y_pos, color='red', linestyle='-', linewidth=0.8)
#gridline space = 0.05
# for i in range(-28, 29):
#     x_pos = i * 0.05
#     ax.axvline(x=x_pos, color='red', linestyle='-', linewidth=0.8)
# for i in range(-28, 29):
#     y_pos = i * 0.05
#     ax.axhline(y=y_pos, color='red', linestyle='-', linewidth=0.8)
#gridline space = 0.03
# for i in range(-47, 48):
#     x_pos = i * 0.03
#     ax.axvline(x=x_pos, color='red', linestyle='-', linewidth=0.8)
# for i in range(-47, 48):
#     y_pos = i * 0.03
#     ax.axhline(y=y_pos, color='red', linestyle='-', linewidth=0.8)
#gridline space = 0.2
for i in range(-8, 9):
    x_pos = i * 0.2
    ax.axvline(x=x_pos, color='red', linestyle='-', linewidth=0.8)
for i in range(-8, 9):
    y_pos = i * 0.2
    ax.axhline(y=y_pos, color='red', linestyle='-', linewidth=0.8)

power = 2
npower = -1*power

for i in range(len(x_points)):
    x = x_points[i]
    y = y_points[i]
    x_min = int(x * pow(10, power)) / (pow(10, power))
    x_max = int((x + pow(10, npower)) * (pow(10, power))) / (pow(10,power))
    y_min = int(y * pow(10, power)) / (pow(10, power))
    y_max = int((y + pow(10, npower)) * pow(10, power)) / (pow(10, power))
    ax.fill_between([x_min, x_max], y_min, y_max, facecolor='k', alpha=1)

#plt.savefig("figures/gridplot_c_equals_0_gridsize_0.05.png")
plt.show()
