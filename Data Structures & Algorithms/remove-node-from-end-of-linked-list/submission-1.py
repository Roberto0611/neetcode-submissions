# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # edge cases

            
        
        # reverse the node
        curr = head
        prev = None
        nxt = head

        while(curr):
            nxt = curr.next

            curr.next = prev
            
            prev = curr
            curr = nxt

        head = prev

        # search the nth number and delete it
        curr = head
        prev = None
        i = 1

        while(i != n):
            prev = curr
            curr = curr.next
            i+=1
        
        if i == 1 and curr.next:
            curr = curr.next
        elif i == 1 and curr.next == None:
            return None
        else:
            prev.next = curr.next
            curr = head

        # reverse the node again    
        prev = None
        nxt = head

        while(curr):
            nxt = curr.next

            curr.next = prev
            
            prev = curr
            curr = nxt

        return prev
        