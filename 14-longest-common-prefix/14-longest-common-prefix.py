class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        try:
            for i in range(len(strs[0])):
                char = strs[0][i]
                for j in range(len(strs)):

                    if strs[j][i] != char:
                        return pre
                pre += char
        finally:
            return pre