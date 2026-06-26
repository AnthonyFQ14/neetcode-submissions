# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodes = []

        def dfs(node, lst):

            if not node:
                return

            lst.append(node.val)
            
            dfs(node.left, lst)
            dfs(node.right, lst)

        dfs(root, nodes)

        nodes.sort()

        print(nodes)

        return nodes[k - 1]