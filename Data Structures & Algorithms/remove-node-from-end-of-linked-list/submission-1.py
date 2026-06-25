# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        indexToRemove = N - n
        
        if indexToRemove == 0:
            return head.next

        index = 0
        curr = head
        while curr:
            if index == indexToRemove - 1:
                curr.next = curr.next.next
            curr = curr.next
            index += 1
        return head







        