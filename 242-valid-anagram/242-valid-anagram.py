class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}
        
        for i, _ in enumerate(s):
            if s[i] in ds:
                ds[s[i]] += 1
            else:
                ds[s[i]] = 1
            
            if t[i] in dt:
                dt[t[i]] += 1
            else:
                dt[t[i]] = 1
        
        for key in ds:
            if key not in dt or dt[key] != ds[key]:
                return False
        return True
        
            