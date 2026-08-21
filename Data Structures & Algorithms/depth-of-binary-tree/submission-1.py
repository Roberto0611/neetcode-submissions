# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for this problem we can use DFS
        def dfs(nodo):
            # checar que hay nodo
            if not nodo:
                return 0

            # contar la profundidad
            izq = dfs(nodo.left)
            der = dfs(nodo.right)

            # devolver profundidad + 1 
            return 1 + max(izq,der)
        
        return dfs(root)

