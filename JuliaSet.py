import numpy as np
import matplotlib.pyplot as plt


def computeIterations(c, z):
    global iterations
    count = 0
    # iterates z unless the number diverges
    for a in range(iterations):
        z = z ** 2 + c  # iteration equation
        count += 1
        # if greater than 4 it can be proven to diverge
        if abs(z) > 4:
            break
    return count


def mandelbrotSet(x, y):
    # initialize new grid
    m = np.zeros((len(x), len(y)))
    # loop through each coordinate
    for i in range(len(x)):
        for j in range(len(y)):
            # define the initial conditions
            c = complex(-0.512511498387847167, 0.521295573094847167)
            z = complex(x[i], y[j])
            # get iteration count
            count = computeIterations(c, z)
            # iteration grids value to be the count
            m[i, j] = count
    return m


# define the resolution and max iterations
rows = 2880
cols = 1800
iterations = 64

# define the domain of the array
x = np.linspace(-1.5, 1.5, rows)
y = np.linspace(-1, 1, cols)

# generate the set
m = mandelbrotSet(x, y)

# make a color map based on iteration value
cmap = plt.get_cmap('Greys')
norm = plt.Normalize(vmin=m.min(), vmax=m.max())

# create the image
image = cmap(norm(m.T))

# save the image
plt.imsave('juliaSet.png', image)
