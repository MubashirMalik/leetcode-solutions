class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return nums1
        
        i = 0
        j = 0
        total =  m + n
        
        nums3 = []
        for _ in range(total):

                
            if i< m and j < n:
                if nums1[i] < nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    nums3.append(nums2[j])
                    j+= 1
            else:
                if i == m:
                    for r in range(j, n):
                        nums3.append(nums2[r])
                    break
                if j == n:
                    for r in range(i, m):
                        nums3.append(nums1[r])
                        print(r)
                        print(nums3)
                    break
            # print(i)
            # print(j)
            # print(nums3)
        for k in range(len(nums3)):
            nums1[k] = nums3[k]
            