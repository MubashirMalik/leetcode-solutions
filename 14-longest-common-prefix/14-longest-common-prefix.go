func longestCommonPrefix(strs []string) string {
    prefix := ""
    if len(strs) == 0 {
        return prefix
    }
    
    for i := 0; i < len(strs[0]); i++ {
        var flag bool
        for j := 1; j < len(strs); j++ {
            if i >= len(strs[j]) {
                flag = true
                break
            }
            
            if strs[j][i] != strs[0][i] {
                return prefix
            }
        }
        
        if !flag {
             prefix += string(strs[0][i])
        }
    }
    return prefix
}