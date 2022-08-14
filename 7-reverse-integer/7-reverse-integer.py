class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            reversed_x = int(x[1:][::-1])
            if reversed_x > 2**31:
                return 0
            return -reversed_x
        else:
            reversed_x = int(x[::-1])
            if reversed_x > 2**31 :
                return 0
            return int(x[::-1])
        