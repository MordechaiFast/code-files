import numpy as np
np.warnings.filterwarnings('ignore')
from PIL import Image

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    real = np.linspace(xmin, xmax, int((xmax-xmin)*pixel_density))
    imagenary = np.linspace(ymin, ymax, int((ymax-ymin)*pixel_density))
    return real[np.newaxis, :] + imagenary[:, np.newaxis]*1j

def is_stable(c: complex, num_iterations: int) -> bool:
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
image = Image.fromarray(~is_stable(c, num_iterations=20))
image.show()