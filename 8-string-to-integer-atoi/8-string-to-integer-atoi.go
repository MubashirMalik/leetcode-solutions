func myAtoi(s string) int {
    
    if len(s) == 0 {
        return 0
    }
    
    var i int
    // step 1
    for i = 0; s[i] == ' '; i++ {
        if i+1 >= len(s) {
            return 0
        }   
    }
    // step 2
    var isNegative bool
    if s[i] == '-' {
        isNegative = true 
        i++
    } else if s[i] == '+' {
        i++
    }
   
    // step 3
    var number string
    for i < len(s) && s[i] >= 48 && s[i] <= 57 {
        number += string(s[i])
        i++
    }
    x, _ := strconv.Atoi(number)
    
    if isNegative {
        x *= -1
    }
    
    // chop chop
    if x > 2147483647 {
        x = 2147483647
    } else if x < -2147483648 {
        x = -2147483648
    }
    
    return x
}