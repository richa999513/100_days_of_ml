#  data visualization - matplotlib
import matplotlib.pyplot as plt
# 1. Line Chart - SYNTAX - matplotlib.pyplot.plot(x, y)

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y)
plt.title("Line Chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()

# 2.Bar Chart - SYNTAX - matplotlib.pyplot.bar(x, height)
x = ['Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190]

plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 3. histogram - SYNTAX - matplotlib.pyplot.hist(x, bins=None)
x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='steelblue')
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot - SYNTAX - matplotlib.pyplot.scatter(x, y)
x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 160, 130, 240, 200]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 5. Pie Chart - Syntax - matplotlib.pyplot.pie(x, labels=None, autopct=None)

# Parameter:
# x: Data values for pie slices.
# labels: Names for each slice.
# autopct: Format to display percentage (e.g., '%1.1f%%').
import pandas as pd

cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars)
plt.title(" Pie Chart")
plt.show()

# 6. Box Plot -Syntax- matplotlib.pyplot.boxplot(x, notch=False, vert=True)

# Parameter:
# x: Data for which box plot is to be drawn (usually a list or array).
# notch: If True, draws a notch to show the confidence interval around the median.
# vert: If True, boxes are vertical. If False, they are horizontal.

data = [ [10, 12, 14, 15, 18, 20, 22],
         [8, 9, 11, 13, 17, 19, 21],
         [14, 16, 18, 20, 23, 25, 27] ]

plt.boxplot(data)
plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

# 7. Heatmap -Syntax- matplotlib.pyplot.imshow(X, cmap='viridis')

# Parameter:
# X: 2D array (data to display as an image or heatmap).
# cmap: Sets the color map.
import numpy as np
np.random.seed(0)
data = np.random.rand(10, 10)

plt.imshow(data, cmap='viridis', interpolation='nearest')

plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Heatmap')
plt.show()
# np.random.seed(0): Ensures same random values every time (reproducibility).
# np.random.rand(10, 10): Generates a 10×10 array of random numbers between 0 and 1.

# 1. Customizing Line Chart
# Color: Change the color of the line
# Linewidth: Adjust the width of the line
# Marker: Change the style of plotted points
# Markersize: Change the size of the markers
# Linestyle: Define the style of the line like solid, dashed, etc.
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y, color='green', linewidth=3, marker='o', markersize=15, linestyle='--')

plt.title("Customizing Line Chart")
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.show()

# 2. Customizing Bar Chart
# Color: Fill color of the bars
# Edgecolor: Color of the bar edges
# Linewidth: Thickness of the edges
# Width: Width of each bar
x = ['Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190]

plt.bar(x, y, color='green', edgecolor='black', linewidth=2)

plt.title("Customizing Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 3. Customizing Histogram Plot
# Bins: Number of groups (bins) to divide data into
# Color: Bar fill color
# Edgecolor: Bar edge color
# Linestyle: Style of the edges like solid, dashed, etc.
# Alpha: Transparency level (0 = transparent, 1 = opaque)

x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17,
     18, 18, 19, 20, 20, 21, 22, 23, 24, 25, 25, 26, 28, 30,
     32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='green', edgecolor='blue',linestyle='--', alpha=0.5)

plt.title("Customizing Histogram Plot")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# 4. Customizing Scatter Plot
# S: Marker size (single value or array)
# C: Color of markers or sequence of colors
# Marker: Marker style like circle, diamond, etc.
# Linewidths: Width of marker borders
# Edgecolor: Color of marker borders
# Alpha: Blending value, between 0 (transparent) and 1 (opaque)
x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 180, 130, 260, 200]
size = [2, 3, 4, 2, 3, 2, 4, 3]  
bill = [170, 120, 250, 190, 180, 130, 260, 200]  

plt.scatter(x, y, c=size, s=bill, marker='D', alpha=0.5)

plt.title("Customizing Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 5. Customizing Pie Chart
# Explode: Moving the wedges of the plot
# Autopct: Label the wedge with their numerical value.
# Color: Colors of the slices
# Sadow: Used to create a shadow effect
import pandas as pd 
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 13, 35, 15, 12]
explode = [0.1, 0.5, 0, 0, 0]
colors = ( "orange", "cyan", "yellow","grey", "green",)

plt.pie(data, labels=cars, explode=explode, autopct='%1.2f%%',colors=colors, shadow=True)
plt.show()

# Matplotlib’s Core Components: Figures and Axes
# 1. Figure class - the Figure class represents the full drawing area or canvas that can hold one or more plots. lets user control the overall size, layout and background of the plot window.
# Syntax: matplotlib.figure.Figure(figsize=None, facecolor=None)
# Parameter:
# figsize: Sets size of the figure (width, height) in inches.
# facecolor: Sets background color of the figure

fig = plt.figure(figsize=(6, 4), facecolor='lightblue')

# Add Axes to the Figure
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
ax.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

# 2. Axes Class-Axes class represents actual plotting area where data is drawn. It is the most basic and flexible for creating plots or subplots within a figure. A single figure can contain multiple axes but each Axes object belongs to only one figure. It can create an Axes object using axes() function.
# Syntax:axes([left, bottom, width, height])
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

fig = plt.figure(figsize=(5, 4))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 

ax.plot(x, y)
ax.plot(y, x)

ax.set_title("Linear Graph")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend(labels=('line 1', 'line 2'))
plt.show()

# Advanced Techniques for Visualizing Subplots
# 1. Using add_axes(): add_axes() method allows us to manually add axes to a figure in Matplotlib. It takes a list of four values [left, bottom, width, height] to specify the position and size of the axes.
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

fig = plt.figure(figsize=(10, 4)) 
ax1 = fig.add_axes([0.1, 0.1, 0.35, 0.8]) 
ax2 = fig.add_axes([0.55, 0.1, 0.35, 0.8])

ax1.plot(x, y)
ax2.plot(y, x)
plt.show()

# 2. Using subplot() - The subplot() method adds a plot to a specified grid position within the current figure. It takes three arguments: the number of rows, columns and plot index.
# Matplotlib’s subplot() takes a 3-digit code (or 3 separate integers) in the form:
#                             mnp
# - m → number of rows in the subplot grid
# - n → number of columns in the subplot grid
# - p → the position index of the subplot (counting left to right, top to bottom)

import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]
plt.figure()

plt.subplot(121)
plt.plot(x, y)

plt.subplot(122)
plt.plot(y, x)
plt.show()

# 3. Using subplot2grid() : The subplot2grid() creates axes object at a specified location inside a grid and also helps in spanning the axes object across multiple rows or columns.
import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

axes1 = plt.subplot2grid (
(7, 1), (0, 0), rowspan = 2, colspan = 1)

axes2 = plt.subplot2grid (
(7, 1), (2, 0), rowspan = 2, colspan = 1)

axes1.plot(x, y)
axes2.plot(y, x)
plt.show()

#  Breaking it down
# - (7, 1) → This defines the grid shape:
# - 7 rows
# - 1 column
# So you’re dividing the figure into a tall vertical grid with 7 slots stacked on top of each other.
# - (0, 0) → This is the starting cell position (row, column):
# - Row index = 0 (the very top row)
# - Column index = 0 (the only column, since you specified 1 column)
# So the subplot begins at the top-left cell of the grid.
# - rowspan=2 → The subplot spans 2 rows downward (rows 0 and 1).
# - colspan=1 → The subplot spans 1 column (just that single column).


# Saving Plots Using savefig() - When plots are created using Matplotlib, users may want to save them as image files for use in reports, presentations or sharing. Matplotlib offers savefig() function to save the current plot to a file. By changing file extension, users can store the plot in different formats such as .png, .jpg, .pdf or .svg.

import matplotlib.pyplot as plt

year = ['2010', '2002', '2004', '2006', '2008']
production = [25, 15, 35, 30, 10]

plt.bar(year, production)

plt.savefig("output.jpg")
plt.savefig("output1", facecolor='y', bbox_inches="tight",pad_inches=0.3, transparent=True)