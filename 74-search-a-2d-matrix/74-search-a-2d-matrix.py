class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            temp = arr
            if target > arr[-1]:
                continue
            elif target == arr[-1]:
                return True
            else:
                if self.binarySearch(temp, target):
                    return True
        return False
        
    def binarySearch(self, arr, item):
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            mid = (i + j)//2
            
            if item > arr[mid]:
                i = mid + 1
            elif item < arr[mid]:
                j = mid - 1
            else:
                return True
            
        return False
        