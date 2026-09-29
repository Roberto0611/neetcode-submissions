# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ITERATIVE SOLUTION
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()

            if not node:
                continue
            
            # swap
            node.left,node.right = node.right,node.left

            # add
            stack.append(node.left)
            stack.append(node.right)

        return root