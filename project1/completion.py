import random
import cut_graph
import numpy as np


def complete(img, size, mode="random"):
    """
    :param img: the src texture
    :param size: size of result (a triple)
    :param mode: mode of patch placement
    :return: the completed image
    """
    completed_img = np.zeros(size)
    patch_height, patch_width, channel = img.shape
    img_height, img_width, img_channel = size
    if mode == "random":
        # flag_matrix: to record the already generated pixels
        flag_matrix = np.zeros((img_height, img_width))
        while np.count_nonzero(flag_matrix) < flag_matrix.size:
            offset_i = 0
            offset_j = 0
            while check_full_overlap(flag_matrix, (offset_i, offset_j), patch_height, patch_width):
                offset_i = int(random.random() * img_height)
                offset_j = int(random.random() * img_width)
            if check_overlap(flag_matrix, (offset_i, offset_j), patch_height, patch_width):

            else:
                real_bottom = min(img_height, offset_i + patch_height)
                real_right = min(img_width, offset_j + patch_width)
                for i in range(offset_i, real_bottom):
                    for j in range(offset_j, real_right):
                        flag_matrix[i][j] = 1
                        completed_img[i][j] = img[i-offset_i][j-offset_j]


    return completed_img


def check_overlap(bit_map, coordinate, patch_height, patch_width):
    """
    :param patch_width: width of the patch
    :param patch_height: height of the patch
    :param bit_map: the old bit map
    :param coordinate: the coordinate (left-top) of the patch to be placed
    :return: whether the patch overlaps the old img
    """
    overlap = False
    height, width = bit_map.shape
    for i in range(patch_height):
        for j in range(patch_width):
            offset_i = i + coordinate[0]
            offset_j = j + coordinate[1]
            if offset_i < height and offset_j < width and bit_map[offset_i][offset_j] == 1:
                overlap = False
                break
    return overlap


def check_full_overlap(bit_map, coordinate, patch_height, patch_width):
    """
    :param bit_map: the old bit map
    :param coordinate: the coordinate (left-top) of the patch to be placed
    :param patch_height: height of the patch
    :param patch_width: width of the patch
    :return: whether the patch if fully covered by the old bit map
    """
    full_overlap = True
    height, width = bit_map.shape
    for i in range(patch_height):
        for j in range(patch_width):
            offset_i = i + coordinate[0]
            offset_j = j + coordinate[1]
            if offset_i < height and offset_j < width and bit_map[offset_i][offset_j] == 0:
                full_overlap = False
                break
    return full_overlap
