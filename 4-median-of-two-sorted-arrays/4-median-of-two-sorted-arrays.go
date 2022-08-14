func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {

    totalLength := len(nums1) + len(nums2) 
    mergedArray := make([]int, totalLength)
    var idx1, idx2 int
    for i := 0; i < totalLength/2 + 1; i++ {    
        var value int
        
        if idx1 < len(nums1) && idx2 < len(nums2) {
            if nums1[idx1] <= nums2[idx2] {
                value = nums1[idx1]
                idx1++
            } else {
                value = nums2[idx2]
                idx2++
            }     
        } else if idx1 < len(nums1) {
            value = nums1[idx1]
            idx1++
        } else {
            value = nums2[idx2]
            idx2++
        }
        
        mergedArray[i] = value 
    } 
    
    if totalLength % 2 == 0 {
        x1 := float64(mergedArray[totalLength/2 - 1])
        x2 := float64(mergedArray[totalLength/2])
        return (x1+x2)/2
    } else {
        return float64(mergedArray[totalLength/2])
    }
}