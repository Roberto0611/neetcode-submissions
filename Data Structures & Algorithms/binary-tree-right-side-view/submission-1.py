# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        # bfs
        if not root:
            return []
            
        queue = deque([root])

        while queue:
            # take picture of queue 
            n = len(queue)

            # iterate through the level and add the first element
            for i in range(n):
                actual = queue.popleft()

                if actual.right:
                    queue.append(actual.right)
                if actual.left:
                    queue.append(actual.left)
                
                # add if first
                if i == 0:
                    output.append(actual.val)
                
        return output