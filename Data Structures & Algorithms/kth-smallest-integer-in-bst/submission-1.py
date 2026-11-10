# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we count in the way back trip
        count = 0
        result = None
        # dfs
        def dfs(root):
            nonlocal count,result

            if not root or result is not None:
                return
            
            dfs(root.left) # start with left  
    
            # return trip
            count += 1

            if count == k:
                result = root.val
                return
            
            dfs(root.right)

        dfs(root);
        return result