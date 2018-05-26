import numpy as np
import scipy.stats
import matplotlib.pyplot as plot

# Get x values of the cosine wave

time = np.arange(0, 20, 0.2);

# Amplitude of the cosine wave is cosine of a variable like time
graph = []
amplitude = np.cos(time)
for e in amplitude:
    rvs = scipy.stats.norm.rvs(loc=0, scale=0.5)
    graph.append(e + rvs)
# Plot a cosine wave using time and amplitude obtained for the cosine wave

plot.plot(time, graph)

# Give a title for the cosine wave plot

plot.title('Ações')

# Give x axis label for the cosine wave plot

plot.xlabel('Time')

# Give y axis label for the cosine wave plot

plot.ylabel('Amplitude = cosine(time)')

# Draw the grid for the graph

plot.grid(True, which='both')

plot.axhline(y=0, color='b')

# Display the cosine wave plot

plot.show()