func twoSum(nums []int, target int) []int {
    
    // map (number => index)
    m := make(map[int]int)
    
    var inverse int
    for i := range nums {
        inverse = target - nums[i]
        if idx, isFound := m[inverse]; isFound {
            return []int{idx, i}
        }
        m[nums[i]] = i
    }
    return []int{0, 0}
}