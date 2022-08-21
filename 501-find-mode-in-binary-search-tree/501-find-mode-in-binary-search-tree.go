/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
    if root.Left == nil && root.Right == nil {
        return []int{root.Val}
    }

    occurrences := make(map[int]int)
    
    var InOrder func(root *TreeNode)
    var max int 
    
    InOrder = func(root *TreeNode) {
        if root == nil {
            return
        }
        
		occurrences[root.Val]++
        if max < occurrences[root.Val] {
            max = occurrences[root.Val]
        }

        InOrder(root.Left)
        InOrder(root.Right)
    }
    InOrder(root)
    
    var modes []int
    for k,v := range occurrences {
        if v == max {
            modes = append(modes, k)
        }
    }
    
    return modes
}