func addDigits(num int) int {
    sum := num
    for num > 9 {
        sum = 0
        for num > 0 {
            sum += num % 10
            num = num / 10
        }
        num = sum
    }
    return sum
}