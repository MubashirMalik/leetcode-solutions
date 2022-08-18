class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        tri = []
        for i in range(1, numRows + 1):
            row = [1] * i
            if i > 2:
                prev = 0
                s = 0
                for j, k in enumerate(tri[-1]):
                    s = prev + k
                    row[j] = s
                    prev = k
                    
                    
            tri.append(row)
        
        return tri