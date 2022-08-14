func lengthOfLongestSubstring(s string) int {
    
    if len(s) == 0 {
        return 0
    }
    
    // Kadane's algorithm
    currentMax := string(s[0])
    globalMax := string(s[0])
    for i := 1; i < len(s); i++ {  
        for j := 0; j < len(currentMax); j++ {
            if s[i] == currentMax[j] {
                currentMax = currentMax[j+1:]
                break
            }
        }
        
        currentMax += string(s[i])
        
        if len(currentMax) > len(globalMax) {
            globalMax = currentMax
        }
    }
    
    return len(globalMax)
}