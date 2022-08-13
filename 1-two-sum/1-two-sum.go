import "sort"

func twoSum(nums []int, target int) []int {
    copyNums := make([]int, len(nums))
    for i := range nums {
        copyNums[i] = nums[i]
    }
    sort.Ints(nums)
    
    var num1, num2 int
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                num1 = nums[i]
                num2 = nums[j]
                break
            }
        }
    }
    
    var idx1, idx2 int
    var isSet bool 
    for i := 0; i < len(copyNums); i++ {
        if copyNums[i] == num1 && !isSet {
            idx1 = i
            isSet = true
        } else if copyNums[i] == num2 {
            idx2 = i
        }
    }
    
    
    return []int{idx1, idx2}
}