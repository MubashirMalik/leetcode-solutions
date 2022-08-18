import numpy as np


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        else:
            new_mat = []
            
            k = 0
            l = 0
            sub_mat = []
            for _, i in enumerate(mat):
                for _, j in enumerate(i):
                    sub_mat.append(j)
                    l += 1
                    if l == c:
                        new_mat.append(sub_mat)
                        sub_mat = []
                        l = 0
                        k +=1
            return new_mat
        