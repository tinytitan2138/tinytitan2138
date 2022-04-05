import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection="3d")

X_data = np.arange(-5, 5, 0.1)
Y_data = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(X_data, Y_data)
Z = np.cos(X) * np.sin(Y)

ax.plot_surface(X, Y, Z, cmap="plasma")
plt.show()
