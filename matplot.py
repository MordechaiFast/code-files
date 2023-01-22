import numpy as np

np.warnings.filterwarnings('ignore')

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    real = np.linspace(xmin, xmax, int((xmax-xmin)*pixel_density))
    imagenary = np.linspace(ymin, ymax, int((ymax-ymin)*pixel_density))
    return real[np.newaxis, :] + imagenary[:, np.newaxis]*1j

def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

c = complex_matrix(0, 0.25, .5, .75, pixel_density=4000)

import matplotlib.pyplot as plot

plot.imshow(is_stable(c, num_iterations=20), cmap='binary')
plot.gca().set_aspect('equal')
plot.axis('off')
plot.tight_layout()
plot.show()


def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]
#members = get_members(c, num_iterations=30)
#plot.scatter(members.real, members.imag, c='black', marker=',', s=1)

def sequence(c, z=0):
    while True:
        yield z
        z = z ** 2 + c

def mandelbrot(candidate):
    return sequence(z=0, c=candidate)

def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)