class Solution:
    def convert(self, s: str, numRows: int) -> str:
       
        if numRows == 1:
            return s
        zigzag = ""
        step = 0
        row = 0
        short_step = 0
        should_short_step = False
        short_taken = False
        for i in range(len(s)):
            zigzag += s[step]
            
            if row == numRows-1:
                should_short_step = False
            
            if should_short_step:
                step += (numRows * 2) - 2 - (row * 2)
                short_taken = True
                should_short_step = False
            else:
                if short_taken:
                    step += row*2
                    short_taken = False
                    should_short_step = True
                else:
                    step += (numRows * 2) - 2 

            
            if step >= len(s):
                row += 1
                step = row
                should_short_step = True
            
            
        return(zigzag)