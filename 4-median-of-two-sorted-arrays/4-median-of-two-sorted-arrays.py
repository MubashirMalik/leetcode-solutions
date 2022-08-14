class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        i = 0
        j = 0
        
        total_len = len(nums1) + len(nums2)
        
        even = True
        if total_len % 2 != 0:
            even = False
        
        med_index = 0
        for _ in range(total_len):
            if i == len(nums1):
                for k in range(j, len(nums2)):
                    merged_list.append(nums2[k])
                    if med_index == total_len//2:
                        if not even:
                            return merged_list[med_index]
                        else:
                            return (merged_list[med_index] + merged_list[med_index-1])/2
                    med_index += 1
                break;
            if j == len(nums2):
                for k in range(i, len(nums1)):
                    merged_list.append(nums1[k])
                    if med_index == total_len//2:
                        if not even:
                            return merged_list[med_index]
                        else:
                            return (merged_list[med_index] + merged_list[med_index-1])/2
                    med_index += 1
                break;
            
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i+= 1
                
            else:
                merged_list.append(nums2[j])
                j+= 1
            
            if med_index == total_len//2:
                if not even:
                    return merged_list[med_index]
                else:
                    return (merged_list[med_index] + merged_list[med_index-1])/2
            med_index += 1
                    
        return -1 
        