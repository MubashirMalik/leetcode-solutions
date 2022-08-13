func longestCommonPrefix(strs []string) string {
    lcp := len(strs[0])
    for i := 1; i < len(strs); i++ {
        count := 0
        for j := 0; j < len(strs[i]) && j < len(strs[0]); j++ {
            if strs[0][j] == strs[i][j] && count < lcp {
                count++
            } else {
                break
            }
        }
        if lcp > count {
            lcp = count
        }
    }
    return strs[0][:lcp]
}