func matrixReshape(mat [][]int, r int, c int) [][]int {
    
    if r * c != len(mat)*len(mat[0]) {
        return mat
    }
    
    newShape := make([][]int, r)
    for i := 0; i < r; i++ {
        newShape[i] = make([]int, c)
    }
    
    var k, l int
    for i := 0; i < len(mat); i++ {
        for j := 0; j < len(mat[i]); j++ {
            newShape[k][l] = mat[i][j]
            l++
            if l == c {
                l = 0
                k++
            }
        } 
    }
    
    return newShape
}