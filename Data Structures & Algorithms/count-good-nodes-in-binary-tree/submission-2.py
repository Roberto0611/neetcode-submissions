# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_val):
            if not root:
                return 0
            
            if(root.val >= max_val):
                is_good = 1
            else:
                is_good = 0

            newMax = max(max_val, root.val)

            return is_good +  dfs(root.right,newMax) + dfs(root.left,newMax)

        return dfs(root,root.val)