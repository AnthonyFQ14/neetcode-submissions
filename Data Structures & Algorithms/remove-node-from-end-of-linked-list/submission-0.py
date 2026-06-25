# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        dummy = ListNode()
        dummy.next = head
        dummy = dummy.next

        while dummy:
            nodes.append(dummy.val)
            dummy = dummy.next
        
        res = ListNode()
        dummy = res
        for i, node in enumerate(nodes):
            if i != (len(nodes) - n):
                res.next = ListNode(node)
                res = res.next
        return dummy.next







        