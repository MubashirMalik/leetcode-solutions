func generate(numRows int) [][]int {
    
    pascalTriangle := make([][]int, numRows)
    for i := 0; i < numRows; i++ {
        pascalTriangle[i] = make([]int, i+1)
    }
    for i := 0; i < numRows; i++ {
        for j := 0; j < i + 1; j++ {
            if j == 0 || j + 1 == i + 1 {
                pascalTriangle[i][j] = 1
            } else {
                pascalTriangle[i][j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
            }
        }
    
    }
    return pascalTriangle   
}