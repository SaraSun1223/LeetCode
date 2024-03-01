# Iteration

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        res = ListNode()
        res.next = head
        cur = res
        while cur.next!=None and cur.next.next!=None:
            next = head.next
            temp = next.next
            cur.next = next
            next.next = head
            head.next = temp
            cur = head
            head = head.next
        return res.next


# Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        next = head.next
        head.next = self.swapPairs(head.next.next)
        next.next = head
        return next


