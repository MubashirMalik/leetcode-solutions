class Solution:
    def containsDuplicate(self, nums: List[int]):
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
                if dic[i] == 2:
                    return True
            else: 
                dic[i] = 1
        return False
        