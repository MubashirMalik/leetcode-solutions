class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(temp) -1
        
        while i < j:
            if temp[i] + temp[j] < target:
                i+=1
            elif temp[i] + temp[j] > target:
                j-=1
            else:
                flag = 0
                n1 = -1
                n2 = -1
                for k in range(len(nums)):
                    if nums[k] == temp[i] and not flag:
                        n1 = k
                        flag = 1
                    elif nums[k] == temp[j]:
                        n2 = k
                return [n1, n2]
                    
        