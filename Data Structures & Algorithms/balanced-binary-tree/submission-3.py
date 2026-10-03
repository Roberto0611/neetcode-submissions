# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' 
For this approach, we use recursivity, we check the depth of each path and compare the diff in each level. To avoid using non local we return "-1" and if we detect that -1 in L or R we just keep skipping.
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            if l == -1:
                return -1

            r = dfs(root.right)
            if r == -1:
                return -1

            if abs(l-r) > 1:
                return -1

            return max(l,r) + 1

        return dfs(root) != -1