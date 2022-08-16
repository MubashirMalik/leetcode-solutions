class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        
        dic = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in dic and dic[x] != i:
                return [i, dic[x]]
            dic[nums[i]] = i
            
                        
        