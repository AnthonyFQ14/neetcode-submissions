# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            if not node:
                return True
            
            if node.left and node.left.val < node.val:
                return True
            else:
                return False

            if node.right and node.right > node.val:
                return True
            else:
                return False

            dfs(root.left)
            dfs(root.right)
        
        return dfs(root)
