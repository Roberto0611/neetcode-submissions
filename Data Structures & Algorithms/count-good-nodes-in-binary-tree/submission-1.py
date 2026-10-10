# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' max var with a hashmap '''
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(root,maxVal,maxMap):
            nonlocal count

            if not root:
                return root,maxVal,maxMap

            # -- down logic --

            # compare with max 
            if root.val >= maxVal:
                #print(f"count {root.val}")
                count += 1
                maxVal = root.val
            
            # register on the hashmap
            maxMap[root.val] = maxMap.get(root.val,0) + 1

            dfs(root.left,maxVal,maxMap)
            dfs(root.right,maxVal,maxMap)

            # -- up logic --

            # remove from the hashmap
            maxMap[root.val] = maxMap.get(root.val,0) - 1
            if maxMap[root.val] == 0:
                del maxMap[root.val]

                if root.val == maxVal:
                    # update maxVal
                    if maxMap: 
                        maxVal = max(maxMap)
                    else:
                        maxVal = 0

            return root,maxVal,maxMap

        output = dfs(root,(root.val - 1),dict())
        return count