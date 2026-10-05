# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # get ancestors
        def ancestors(root, find, ancestorsList=None):

            if ancestorsList is None:
                ancestorsList = []
            
            if not root:
                return False

            if root.val == find:
                ancestorsList.append(root)
                return ancestorsList
            
            l = ancestors(root.left,find,ancestorsList)
            if l:
                ancestorsList.append(root)
                return ancestorsList
            r = ancestors(root.right,find,ancestorsList)
            if r:
                ancestorsList.append(root)
                return ancestorsList

            return l or r

        ans1 = ancestors(root,p.val)
        ans2 = ancestors(root,q.val)

        for ans in ans1:
            if ans in ans2:
                return ans
        
        return -1
        