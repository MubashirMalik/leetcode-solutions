class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        index = 0
        count = len(strs)
        pre = ""
        
        while True:
            dic = {}
            for string in strs:
                if len(string) == 0:
                    return ""
                if index < len(string):
                    char = string[index]
                else:
                    return pre
                if char in dic.keys():
                    dic[char] += 1
                else:
                    dic[char] = 1
            if dic[list(dic.keys())[0]] == count:
                pre += list(dic.keys())[0]
            else:
                return pre
            index += 1
                    
                