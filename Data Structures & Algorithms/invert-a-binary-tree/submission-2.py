# Definition for a binary root node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[rootNode]) -> Optional[rootNode]:
        if not root:
            return

        # invert the childrens nodes before adding calling the recursion 
        aux = root.left
        root.left = root.right
        root.right = aux

        # Recursion 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root