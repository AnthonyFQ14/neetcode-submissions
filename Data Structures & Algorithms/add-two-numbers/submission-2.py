# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        first = deque()
        second = deque()

        cur = l1
        while cur:
            first.appendleft(cur.val)
            cur = cur.next
        
        cur = l2
        while cur:
            second.appendleft(cur.val)
            cur = cur.next

        f = ""
        for num in first:
            f += str(num)
        
        s = ""
        for num in second:
            s += str(num)
        
        added = int(f) + int(s)
        
        added = [int(d) for d in str(added)]
        added.reverse()

        cur = ListNode()
        dummy = cur
        for digit in added:
            cur.next = ListNode(digit)
            cur = cur.next
        return dummy.next








