import matplotlib.pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
comparisons = 0
title = "Insertion Sort"
graph = plt.scatter


# Plot data set and variable to highlight
def Plot(highlight, data):
    x = list(range(len(data)))
    global comparisons
    comparisons += 1

    if graph == plt.bar:
        colors = list(len(data) * 'b')
        colors[highlight] = 'r'
        graph(x, data, color=colors)

    if graph == plt.scatter:
        graph(x, data, c=data, cmap='nipy_spectral')

    plt.title(title)
    plt.xlabel('Data size:{}, Number of comparisons:{}'.format(len(data), comparisons))

    camera.snap()