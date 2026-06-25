"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldNodes = { None : None }

        cur = head
        while cur:
            oldNodes[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = oldNodes[cur]
            copy.next = oldNodes[cur.next]
            copy.random = oldNodes[cur.random]
            cur = cur.next

        return oldNodes[head]
