# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        d = {}

        current = head
        index = 0

        while current:
        
            if current.val in d:
                return True
            else:
                d[current.val] = index
            
            current = current.next
            index += 1

        return False