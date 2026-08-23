# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            # viaje de ida
            if not node:
                return 0
            
            left = dfs(node.left)
            rigth = dfs(node.right)

            # viaje de vuelta
            diameter = max(diameter,left + rigth)
            return 1 + max(left,rigth)

        dfs(root)
        return diameter