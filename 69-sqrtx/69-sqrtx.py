class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        i = 0
        j = x
        
        while True:
            mid = (i + j) // 2
            if mid * mid > x:
                j = mid
            elif mid * mid < x:
                i = mid
            else:
                return mid
            if abs(j-i) == 1:
                return min(j, i)
                
            
        
        