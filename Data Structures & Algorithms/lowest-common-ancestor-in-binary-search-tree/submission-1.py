# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' Second approach, here we are going to take advantage of the mathematics behind the binary search tree. If a split happens (p > node and q > node) the actual node is the lowest common ancestor, if p and q > node we search on the right subtree and if p and q < node we search on the right tree'''

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print('recursion')
        if not root:
            return

        if p.val > root.val and q.val > root.val:
            # search on right
            return self.lowestCommonAncestor(root.right,p,q)

        elif p.val < root.val and q.val < root.val:
            # search on left
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root