# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            # if both nulls
            if not p and not q:
                return True

            # if one of them is null or the value is dif
            if not p or not q or p.val != q.val:
                return False

            return isSameTree(p.right,q.right) and isSameTree(q.left,p.left)
        
        # we search for the subRoot value in Root
        if not subRoot:
            if not root:
                return True
            else:
                return False
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            # found it so we check if they are the same
            if isSameTree(root,subRoot):
                return True
        
        l = self.isSubtree(root.left,subRoot)
        if l:
            return True
        r = self.isSubtree(root.right,subRoot)
        if r:
            return True

        return l or r 