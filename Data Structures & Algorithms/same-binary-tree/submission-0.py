# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return 1
            
            if not p or not q:
                return -1
            
            if p.val != q.val:
                return -1

            # iterate
            l = dfs(p.right,q.right)
            if l == -1:
                return -1
            r = dfs(p.left,q.left)
            if r == -1:
                return -1

            return 1;
            
        return dfs(p,q) != -1