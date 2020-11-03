import random
import cut_graph
import numpy as np


def complete(img, size, mode="random"):
    """
    :param img: the src texture
    :param size: size of result
    :param mode: mode of patch placement
    :return: the completed image
    """
    completed_img = np.zeros(size)
    height, width, channel = img.shape
    if mode == "random":
        # flag_matrix: to record the already generated pixels
        flag_matrix = np.zeros((height, width))
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
