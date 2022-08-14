# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        carry = 0
        flag = 0
        temp = ListNode()
        total = temp
        while l1 != None or l2!= None:
            
            n1 = 0
            n2 = 0
            if l1 != None:
                n1 = l1.val
                l1 = l1.next
            if l2 != None: 
                n2 = l2.val
                l2 = l2.next
        
            
            addition = n1 + n2 + carry
            to_add = 0
            if addition > 9:
                carry = 1
                to_add = int(str(addition)[1])
            else:
                carry = 0
                to_add = int(addition)
            
            if flag == 0:
                flag = 1
                temp = ListNode(to_add)
                total = temp
            else:
                temp.next = ListNode(to_add)
                temp = temp.next
                
            
            
        if carry == 1:
            temp.next = ListNode(val=1)
        return total
            
        
            
            