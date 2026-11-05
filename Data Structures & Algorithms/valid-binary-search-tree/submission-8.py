# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
For this approach the key is having an upper and lower limit, when we move to the left we update the upper limit, and when we go to the right we update the lower limit.
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root,mayor,menor):
            if not root:
                return True
            
            # comprobar si esta dentro de los limites
            if mayor is not None:
                if mayor <= root.val:
                    #print(f'a {root.val}, menor: {menor}, mayor: {mayor}')
                    return False

            if menor is not None:
                if menor >= root.val:
                    #print(f'{root.val}, menor: {menor}, mayor: {mayor}')
                    return False

            # llamar a las proximos
            return isBST(root.left,root.val,menor) and isBST(root.right,mayor,root.val)

        return isBST(root,None,None);
