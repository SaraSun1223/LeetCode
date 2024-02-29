# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = l1.val + l2.val
        next1 = total//10
        res = ListNode(total%10)
        if (l1.next or l2.next or next1):
            if(l1.next):
                l1=l1.next
            else:
                l1 = ListNode(0)
            if(l2.next):
                l2=l2.next
            else:
                l2 = ListNode(0)
            l1.val = l1.val + next1
            res.next = self.addTwoNumbers(l1,l2)
        return res