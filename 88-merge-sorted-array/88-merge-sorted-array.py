class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return nums1
        
        total = m + n
        m-=1
        n-=1
        
        for i in range(total-1, -1, -1):
            if m >= 0 and n >=0:
                if nums1[m] > nums2[n]:
                    nums1[i] = nums1[m]
                    m-=1
                else:
                    nums1[i] = nums2[n]
                    n-=1
            else:
                if m == -1 and n == -1:
                    return nums1
                elif m == -1:
                    nums1[i] = nums2[n] 
                    n -=1
                else:
                    nums1[i] = nums1[m]
                    m -=1
                
                
        
        
        
            