func containsDuplicate(nums []int) bool {
    m := make(map[int]bool)
    for i := range nums {
        if _, isFound := m[nums[i]]; isFound {
            return true
        }
        m[nums[i]] = true
    }
    return false
}