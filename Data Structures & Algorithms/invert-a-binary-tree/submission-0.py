# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        mainRoot = root

        if not root:
            return

        # invertir el nivel
        temp = root.left
        root.left = root.right
        root.right = temp

        # pasar al siguiente nivel

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root