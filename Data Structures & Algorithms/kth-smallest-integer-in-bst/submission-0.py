# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we count in the way back trip
        finded = False
        count = 0
        element = None
        # dfs
        def dfs(root, k):
            nonlocal count,finded,element

            if not root:
                return
            
            dfs(root.left,k) # start with left

            # return trip
            count += 1
            print(f'{root.val}: {count}')

            if count == k:
                element = root.val
                finded = True
                return
            
            dfs(root.right,k)

            return

        dfs(root,k);
        return element