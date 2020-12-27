import numpy as np


def delete_seam(img_matrix, energy_matrix, orient):
    """
    delete one seam from the given img
    :param img_matrix: the given img
    :param energy_matrix: the energy matrix of the given img
    :param orient: horizontal or vertical seam to be deleted
    :return: the img which has been deleted one seam
    """
    height, width, channel = img_matrix.shape
    if orient == 'horizontal':
        ret_matrix = np.zeros((height-1, width, channel))
        route_matrix = np.zeros(energy_matrix.shape)
        for i in range(1, width):
            for j in range(height):
                if j == 0:
                    if energy_matrix[j][i-1] < energy_matrix[j+1][i-1]:
                        energy_matrix[j][i] += energy_matrix[j][i-1]
                        route_matrix[j][i] = j
                    else:
                        energy_matrix[j][i] += energy_matrix[j+1][i-1]
                        route_matrix[j][i] = j+1
                elif j == height-1:
                    if energy_matrix[j][i-1] < energy_matrix[j-1][i-1]:
                        energy_matrix[j][i] += energy_matrix[j][i-1]
                        route_matrix[j][i] = j
                    else:
                        energy_matrix[j][i] += energy_matrix[j-1][i-1]
                        route_matrix[j][i] = j-1
                else:
                    if energy_matrix[j-1][i-1] <= energy_matrix[j][i-1] and energy_matrix[j-1][i-1] <= energy_matrix[j+1][i-1]:
                        energy_matrix[j][i] += energy_matrix[j-1][i-1]
                        route_matrix[j][i] = j-1
                    elif energy_matrix[j][i-1] <= energy_matrix[j-1][i-1] and energy_matrix[j][i-1] <= energy_matrix[j+1][i-1]:
                        energy_matrix[j][i] += energy_matrix[j][i-1]
                        route_matrix[j][i] = j
                    else:
                        energy_matrix[j][i] += energy_matrix[j+1][i-1]
                        route_matrix[j][i] = j+1

        min_energy = energy_matrix[0][width-1]
        min_index = 0
        for i in range(height):
            if energy_matrix[i][width-1] < min_energy:
                min_energy = energy_matrix[i][width-1]
                min_index = i

        for i in range(width):
            for j in range(height-1):
                if j < min_index:
                    for c in range(channel):
                        ret_matrix[j][width-1-i][c] = img_matrix[j][width-1-i][c]
                else:
                    for c in range(channel):
                        ret_matrix[j][width-1-i][c] = img_matrix[j+1][width-1-i][c]
            min_index = route_matrix[int(min_index)][int(width-1-i)]

        return ret_matrix
    elif orient == 'vertical':
        return img_matrix
    else:
        return img_matrix
