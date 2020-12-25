from PIL import Image
import numpy as np


if __name__ == '__main__':
    img = Image.open('data/test.jpg')
    img = np.array(img)
    print(img.shape)



