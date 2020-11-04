import numpy as np


class CutGraph:
    # store the index of vertexes
    # -1: the index of the virtual vertex representing the old img
    # -2: the index of the virtual vertex representing the new patch
    vertex_set = [-1, -2]
    # store the coordinate (i, j, flag) of vertexes
    coordinate_set = []
    # store the sides
    side_set = []

    def add_vertex(self, coordinate_i, coordinate_j):
        self.vertex_set.append(len(self.coordinate_set))
        self.coordinate_set.append((coordinate_i, coordinate_j))

    def measure(self, src_coordinate, dst_coordinate, img, patch, offset_i, offset_j):
        img_length = np.linalg.norm(img[src_coordinate[0]][src_coordinate[1]] - img[dst_coordinate[0]][dst_coordinate[1]])
        patch_length = np.linalg.norm(patch[src_coordinate[0]-offset_i][src_coordinate[1]-offset_j] - patch[dst_coordinate[0]-offset_i][dst_coordinate[1]-offset_j])
        return img_length + patch_length

    def generate_sides(self, img, patch, offset_i, offset_j):
        """

        :param offset_j: the offset of patch (in x axis)
        :param offset_i: the offset of patch (in y axis)
        :param img: the already generated image np.array((x, y, 3))
        :param patch: the patch
        :return: none
        """
        patch_height, patch_width, channel = patch.shape
        img_height, img_width, img_channel = img.shape
        for i in range(len(self.coordinate_set)):
            current_vertex = self.coordinate_set[i]
            if current_vertex[2] == 1:
                self.side_set.append(Side(i, -1, float("inf")))
            if current_vertex[2] == 2:
                self.side_set.append(Side(i, -2, float("inf")))
            for j in range(i, len(self.coordinate_set)):
                dst_coordinate = self.coordinate_set[j]
                if ((current_vertex[0]==dst_coordinate[0] and current_vertex[1]==dst_coordinate[1]+1) or
                        (current_vertex[0]==dst_coordinate[0] and current_vertex[1]==dst_coordinate[1]-1) or
                        (current_vertex[1]==dst_coordinate[1] and current_vertex[0]==dst_coordinate[0]-1) or
                        (current_vertex[1]==dst_coordinate[1] and current_vertex[0]==dst_coordinate[0]+1)):
                    self.side_set.append(Side(i, j, self.measure(current_vertex, dst_coordinate, img, patch, offset_i, offset_j)))

    def cut(self):
        


class Side:
    index_start = 0
    index_end = 0
    weight = 0

    def __init__(self, index_1, index_2, weight):
        self.index_start = index_1
        self.index_end = index_2
        self.weight = weight

