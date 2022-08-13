func maxSubArray(nums []int) int {
    var prevSum int
    var maxSum int
    for i := range nums {
        if i == 0 {
            prevSum = nums[i]
            maxSum = nums[i]
            continue
        } 
        if prevSum + nums[i] < nums[i] {
            prevSum = nums[i]
        } else {
            prevSum += nums[i]
        }
        
        if maxSum < prevSum {
            maxSum = prevSum
        }
    }
    return maxSum
}