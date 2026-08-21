# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for this problem we can use DFS
        depth = 0

        def dfs(nodo):
            # checar que hay nodo
            if not nodo:
                return 0

            izq = dfs(nodo.left)
            der = dfs(nodo.right)

            return 1 + max(izq,der)
        
        return dfs(root)

