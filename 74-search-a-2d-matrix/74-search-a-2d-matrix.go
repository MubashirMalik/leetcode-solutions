func searchMatrix(matrix [][]int, target int) bool {
 
    for i := 0; i < len(matrix); i++ {
        j := len(matrix[i]) - 1
        
        if matrix[i][j] == target {
            return true
        }
        
        var left, right, mid int
        if matrix[i][j] > target { 
            left = 0
            right = j
            for right >= left {
                mid = (right + left) /2 
                if matrix[i][mid] == target {
                    return true   
                } else if matrix[i][mid] < target {
                    left = mid + 1
                } else {
                    right = mid - 1
                }
            } 
            return false
        }       
    }
    return false
}