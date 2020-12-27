import numpy as np


def calc_energy_matrix(img_matrix):
    """
    calculate the energy matrix of the given matrix, using Sobel operator
    :param img_matrix: numpy matrix of the img
    :return: numpy matrix of energy
    """
    height, width, channel = img_matrix.shape
    energy_matrix = np.zeros((height, width))
    for i in range(1, height-1):
        for j in range(1, width-1):
            grad_x = 0
            grad_y = 0
            for c in range(channel):
                grad_x = img_matrix[i-1][j-1][c]+2*img_matrix[i-1][j][c]+img_matrix[i-1][j+1][c]-img_matrix[i+1][j-1][c]-2*img_matrix[i+1][j][c]-img_matrix[i+1][j+1][c]
                grad_y = img_matrix[i-1][j+1][c]+2*img_matrix[i][j+1][c]+img_matrix[i+1][j+1][c]-img_matrix[i-1][j-1][c]-2*img_matrix[i][j-1][c]-img_matrix[i+1][j-1][c]
            energy_matrix[i][j] = abs(grad_x)+abs(grad_y)

    for i in range(width):
        energy_matrix[0][i] = energy_matrix[1][i]
        energy_matrix[height-1][i] = energy_matrix[height-2][i]
    for i in range(1, height-1):
        energy_matrix[i][0] = energy_matrix[i][1]
        energy_matrix[i][width-1] = energy_matrix[i][width-2]

    return energy_matrix
