/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
  
    carry := 0
    var sumHead *ListNode
    var sumPrev *ListNode
    for l1 != nil || l2 != nil {
        var v1, v2 int
        if l1 != nil {
            v1 = l1.Val
        } 
        if l2 != nil {
            v2 = l2.Val
        }
        
        newNode := &ListNode{}
        newNode.Val = v1 + v2 + carry
        if newNode.Val >= 10 {
            newNode.Val = newNode.Val % 10
            carry = 1
        } else {
            carry = 0
        }
        
        if sumPrev != nil {
            sumPrev.Next = newNode
        }
        
        // set head of sum list
        if sumHead == nil {
            sumHead = newNode
        } 
        
        sumPrev = newNode
        if l1 != nil {
            l1 = l1.Next
        } 
        if l2 != nil {
            l2 = l2.Next
        }
    }    
    
    if carry == 1 {
        newNode := &ListNode{1, nil}
        sumPrev.Next = newNode
    }
    
    return sumHead
}