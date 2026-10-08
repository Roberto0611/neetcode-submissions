# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' For this approach we use BFS, we take get the length of the queue at the start and that's going to be the number of elements in the next level, we iterate for i in range(n) (n is the length of the queue) and that means we finish a level so we take the length again '''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        # Bfs

        # empty?
        if not root:
            return []

        # queue
        queue = deque([root])

        # main loop
        while queue:
            # take stack picture
            n = len(queue)
            output.append([])

            for i in range(n):
                node = queue.popleft()

                output[-1].append(node.val)
                
                # add childs to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
        return output