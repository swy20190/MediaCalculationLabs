from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def show_image(img, zoom=2.0):
    dpi = 77
    plt.figure(figsize=(img.shape[0]*zoom / dpi, img.shape[0]*zoom / dpi))
    if len(img.shape) == 2:
        img = np.repeat(img[:, :, np.newaxis], 3, 2)
    plt.imshow(img, interpolation='nearest')

