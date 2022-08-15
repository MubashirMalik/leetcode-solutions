func convert(s string, numRows int) string {
 
    if numRows == 1 {
        return s
    }
    
    zigzagStr := ""
    increment := 2*(numRows-1)
    for row := 0; row < numRows; row++ {
        for i := row; i < len(s); i += increment {
            zigzagStr += string(s[i])
            if row > 0 && row < numRows-1 && i+increment-2*row < len(s) {
                zigzagStr += string(s[i+increment-2*row])
            }
        }
    }
    
    return zigzagStr
}