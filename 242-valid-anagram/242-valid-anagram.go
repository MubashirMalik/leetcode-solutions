func isAnagram(s string, t string) bool {
    
    if len(s) != len(t) {
        return false
    }
    
    m := make(map[byte]int)
    for i := range s {
        m[s[i]]++
    }
    
    for i := range t {
        if _, isFound := m[t[i]]; isFound {
            if m[t[i]] == 1 {
                delete(m, t[i])
            } else {
                m[t[i]]--   
            }
            continue
        } 
        return false
    }
    return true
}