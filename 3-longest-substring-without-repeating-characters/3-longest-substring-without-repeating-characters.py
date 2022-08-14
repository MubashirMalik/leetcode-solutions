class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Kadane's algorithm
        
        if len(s) == 0:
            return 0
        max_current = s[0]
        max_global = s[0]
        
        for i in range(1, len(s)):
            if s[i] in max_current:
                
                starting_index = max_current.index(s[i])
                max_current = max_current[max_current.index(s[i]) + 1: i] + s[i]
            else:
                max_current += s[i]
            
            if len(max_current) > len(max_global):
                max_global = max_current
        return len(max_global)
            
        
    
    