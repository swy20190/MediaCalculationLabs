from PIL import Image
import numpy as np
from seam import delete_seam
from img_energy import calc_energy_matrix


if __name__ == '__main__':
    src_img = input("Please enter the name of source image:")
    new_width = int(input("Please enter the width of target image:"))
    new_height = int(input("Please enter the height of target image:"))

    img = Image.open('data/'+src_img)
    img = np.array(img)
    old_height, old_width, channel = img.shape
    for i in range(old_width - new_width):
        energy_matrix = calc_energy_matrix(img)
        img = delete_seam(img, energy_matrix, 'vertical')

    for i in range(old_height - new_height):
        energy_matrix = calc_energy_matrix(img)
        img = delete_seam(img, energy_matrix, 'horizontal')

    img = Image.fromarray(np.uint8(img))
    img.show()
    img.save("output/"+src_img)
