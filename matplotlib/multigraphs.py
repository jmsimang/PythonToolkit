import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt3
import numpy as np

# 1. Multiple graph plot using axes
year = np.array([1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986,
                 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011])
physical_science = np.array([13.8, 14.9, 14.8, 16.5, 18.2, 19.1, 20.0, 21.3, 22.5, 23.7, 24.6, 25.7, 27.3, 27.6, 28.0,
                             27.5, 28.4, 30.4, 29.7, 31.3, 31.6, 32.6, 32.6, 33.6, 34.8, 35.9, 37.3, 38.3, 39.7, 40.2,
                             41.0, 42.2, 41.1, 41.7, 42.1, 41.6, 40.8, 40.7, 40.7, 40.7, 40.2, 40.1])
computer_science = np.array([13.6, 13.6, 14.9, 16.4, 18.9, 19.8, 23.9, 25.7, 28.1, 30.2, 32.5, 34.8, 36.3, 37.1, 36.8,
                             35.7, 34.7, 32.4, 30.8, 29.9, 29.4, 28.7, 28.2, 28.5, 28.5, 27.5, 27.1, 26.8, 27.0, 28.1,
                             27.7, 27.6, 27.0, 25.1, 22.2, 20.6, 18.6, 17.6, 17.8, 18.1, 17.6, 18.2])
health = np.array(
    [77.1, 75.5, 76.9, 77.4, 77.9, 78.9, 79.2, 80.5, 81.9, 82.3, 83.5, 84.1, 84.4, 84.6, 85.1, 85.3, 85.7, 85.5, 85.2,
     84.6, 83.9, 83.5, 83.0, 82.4, 81.8, 81.5, 81.3, 81.9, 82.1, 83.5, 83.5, 85.1, 85.8, 86.5, 86.5, 86.0, 85.9, 85.4,
     85.2, 85.1, 85.0, 84.8])

education = np.array(
    [74.53532758, 74.14920369, 73.55451996, 73.50181443, 73.33681143, 72.80185448, 72.16652471, 72.45639481,
     73.19282134, 73.82114234, 74.98103152, 75.84512345, 75.84364914, 75.95060123, 75.86911601, 75.92343971,
     76.14301516, 76.96309168, 77.62766177, 78.11191872, 78.86685859, 78.99124597, 78.43518191, 77.26731199,
     75.81493264, 75.12525621, 75.03519921, 75.1637013, 75.48616027, 75.83816206, 76.69214284, 77.37522931,
     78.64424394, 78.54494815, 78.65074774, 79.06712173, 78.68630551, 78.72141311,
     79.19632674, 79.5329087, 79.61862451, 79.43281184])

# Create plot axes for the first line plot
plt2.axes([0.05, 0.05, 0.425, 0.9])
plt2.plot(year, physical_science, color='blue')
# Create plot axes for the second line plot
plt2.axes([0.525, 0.05, 0.425, 0.9])
plt2.plot(year, computer_science, color='red')
# Display the plot
plt2.show()
plt2.savefig('multigraphs.png')

# 2. Multiple graph plots using subplot - 1 row, 2 columns
# Create a figure with 1x2 subplot and make the left subplot active
plt3.subplot(1, 2, 1)
# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt3.plot(year, physical_science, color='blue')
plt3.title('Physical Sciences')

# Make the right subplot active in the current 1x2 subplot grid
plt3.subplot(1, 2, 2)

# Plot in red the % of degrees awarded to women in Computer Science
plt3.plot(year, computer_science, color='red')
plt3.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt3.tight_layout()
plt3.show()
plt3.savefig('multigraphs-subplots-1x2.png')

# 3. Multiple graph plots using subplot - 2 rows, 2 columns
# Create a figure with 2x2 subplot layout and make the top left subplot active
plt.subplot(2, 2, 1)

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_science, color='blue')
plt.title('Physical Sciences')

# Make the top right subplot active in the current 2x2 subplot grid
plt.subplot(2, 2, 2)

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Make the bottom left subplot active in the current 2x2 subplot grid
plt.subplot(2, 2, 3)

# Plot in green the % of degrees awarded to women in Health Professions
plt.plot(year, health, color='green')
plt.title('Health Professions')

# Make the bottom right subplot active in the current 2x2 subplot grid
plt.subplot(2, 2, 4)

# Plot in yellow the % of degrees awarded to women in Education
plt.plot(year, education, color='yellow')
plt.title('Education')

# Improve the spacing between subplots and display them
plt.tight_layout()
plt.show()
plt.savefig('multigraphs-subplots-2x2.png')
