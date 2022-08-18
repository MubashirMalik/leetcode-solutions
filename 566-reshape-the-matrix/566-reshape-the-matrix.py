import numpy as np


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        else:
            new_mat = [*map(lambda a: [a]*c,[0]*r)]
            
            k = 0
            l = 0
            for i in mat:
                for j in i:
                    new_mat[k][l] = j
                    l += 1
                    if l == c:
                        l = 0
                        k +=1
            return new_mat
        