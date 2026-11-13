# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
        # build hashmap with the index of every element in inorder, 
        # this way we can search the indexes in O(1)

        idx = {val: i for i,val in enumerate(inorder)} # {key:value loop}
        self.pre = 0 # pointer to know which preorder element we are on

        def build(left,right):

            if left > right: # if the array is empty
                return None

            root = TreeNode(preorder[self.pre]) # create the node 

            self.pre+=1    

            # find index of root in inorder
            n = idx[root.val]

            # call left and right using index's instead of slice lists
            root.left = build(left,n - 1)
            root.right = build(n+1, right)

            return root 
            
        return build(0,len(inorder) - 1);