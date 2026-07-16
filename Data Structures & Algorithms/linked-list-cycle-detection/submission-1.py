# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## Mi primer approach es este, luego iteramos en mejoras
        # cada nodo lo guardas en visited y luego cada ves que te mueves comparar
        dummy = ListNode()
        visited = []
        isLoop = False

        while head:
            if head in visited:
                isLoop = True
                break
            visited.append(head)
            head = head.next

        return isLoop