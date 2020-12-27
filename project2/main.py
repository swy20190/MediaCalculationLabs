from PIL import Image
import numpy as np
from seam import delete_seam
from img_energy import calc_energy_matrix


if __name__ == '__main__':
    img = Image.open('data/destroyer.jpg')
    img = np.array(img)
    for i in range(200):
        energy_matrix = calc_energy_matrix(img)
        img = delete_seam(img, energy_matrix, 'vertical')
        print(i)

    img = Image.fromarray(np.uint8(img))
    img.show()
    img.save("output/destroyer.jpg")
