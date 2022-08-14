import "math"
func reverse(x int) int {
 
    var isNegative bool
    if x < 0 {
        x *= -1
        isNegative = true
    }
    
    var numDigits int
    digits := []int{}
    for x > 0 {
        digits = append(digits, x % 10)
        numDigits++
        x /= 10
    }
    
    i := 0
    for numDigits > 0 {
        x += digits[i] * int(math.Pow(10, float64(numDigits-1)))
        i++
        numDigits--
    }
    
    if x > 2147483647 {
        return 0
    }
    
    if isNegative {
        x *= -1
    }
    
    return x
}