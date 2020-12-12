import completion
import numpy as np
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

if __name__ == '__main__':
    src_image1 = mpimg.imread("data/green.gif")
    result1 = completion.complete(src_image1, (128, 128, 4))
    img_output1 = Image.fromarray(result1, mode='RGBA')
    img_output1.save("data/new_green.gif")

    src_image2 = mpimg.imread("data/akeyboard_small.gif")
    result2 = completion.complete(src_image2, (512, 512, 4))
    img_output2 = Image.fromarray(result2, mode='RGBA')
    img_output2.save("data/new_akeyboard_small.gif")

    src_image3 = mpimg.imread("data/strawberries2.gif")
    result3 = completion.complete(src_image3, (512, 512, 4))
    img_output3 = Image.fromarray(result3, mode='RGBA')
    img_output3.save("data/new_strawberries2.gif")


