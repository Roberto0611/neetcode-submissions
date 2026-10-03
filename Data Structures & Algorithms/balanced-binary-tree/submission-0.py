# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root):
            nonlocal balanced
            
            if not root:
                return 0
            
            l = dfs(root.left) 
            r = dfs(root.right)

            print(abs(l-r))
            
            if (abs(l-r)) > 1:
                # el arbol no esta balanceado
                balanced = False 

            return max(l,r) + 1

        dfs(root)
        return balanced