class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_total = 0
        global_total = nums[0]
        
        for i in range(len(nums)):
            max_total = max(nums[i], nums[i] + max_total)
            
            
            if max_total > global_total:
                global_total = max_total
            
        return global_total