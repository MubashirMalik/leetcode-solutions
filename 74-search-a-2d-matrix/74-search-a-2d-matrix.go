func searchMatrix(matrix [][]int, target int) bool {
 
    for i := 0; i < len(matrix); i++ {
        j := len(matrix[i]) - 1
        
        if matrix[i][j] == target {
            return true
        }
        
        if matrix[i][j] > target {
            for j = 0; j < len(matrix[i]); j++ {
                if matrix[i][j] == target {
                    return true
                } 
            }     
        }       
    }
    return false
}