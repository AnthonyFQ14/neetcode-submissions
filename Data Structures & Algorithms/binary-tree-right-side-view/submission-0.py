# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()

        bl = []

        if root:
            q.append(root)


        while len(q) > 0:
            l = []
            for i in range(len(q)):
                curr = q.popleft()
                l.append(curr.val)

                if curr.right:
                    q.append(curr.right)

                if curr.left:
                    q.append(curr.left)
            bl.append(l)

        res = []
        for l in bl:
            res.append(l[0])
        return res

