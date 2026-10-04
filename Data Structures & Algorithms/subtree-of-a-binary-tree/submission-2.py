# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' For this approach first we use dfs to travel into the tree, when we find a node that's equal to the
head of subroot, we use isSameTree to check if thay are equal perse a subtree. The difference with solution 1
is the code its more clean'''

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            # if both nulls
            if not p and not q:
                return True

            # if one of them is null or the value is dif
            if not p or not q or p.val != q.val:
                return False

            return isSameTree(p.right,q.right) and isSameTree(p.left,q.left)
        
        # we search for the subRoot value in Root
        if not subRoot:
            return True # if the subRoot is null its always going to be in the tree
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            # found it so we check if they are the same
            if isSameTree(root,subRoot):
                return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
