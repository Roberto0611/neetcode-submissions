# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## Mi segundo approach es este
        # en lugar de usar un array usas un diccionario
        dummy = ListNode()
        visited = {}
        isLoop = False

        while head:
            if head in visited:
                isLoop = True
                break
            visited[head] = head.val
            head = head.next

        return isLoop