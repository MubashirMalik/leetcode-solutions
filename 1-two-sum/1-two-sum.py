class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic and dic[target - nums[i]] != i:
                return [i, dic[target - nums[i]]]
            dic[nums[i]] = i
            
                        
        