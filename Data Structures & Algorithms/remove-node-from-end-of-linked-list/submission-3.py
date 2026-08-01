# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first we add a dummy node
        dummy = ListNode()
        dummy.next = head

        # two pointers with n distance
        left = dummy
        rigth = head

        for i in range(n):
            rigth = rigth.next
        
        # loop of pointers
        while(rigth):
            rigth = rigth.next
            left = left.next
        
        # update next
        if left.next.next:
            left.next = left.next.next
        else:
            left.next = None
        
        return dummy.next
