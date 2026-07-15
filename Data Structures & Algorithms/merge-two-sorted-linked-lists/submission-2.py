# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head3 = None
        # find the fist value
        
        if curr1 == None and curr2 == None:
            return
        elif curr1 == None:
            head3 = curr2
            curr2 = curr2.next
        elif curr2 == None:
            head3 = curr1
            curr1 = curr1.next
        elif curr1.val >= curr2.val:
            head3 = curr2
            curr2 = curr2.next
        else:
            head3 = curr1
            curr1 = curr1.next

        node = head3
        debug = head3.next

        while curr1 != None or curr2 != None:
            if curr1 == None:
                node.next = curr2
                curr2 = curr2.next
            elif curr2 == None:
                node.next = curr1
                curr1 = curr1.next
            elif curr1.val >= curr2.val:
                node.next = curr2
                curr2 = curr2.next
            else:
                node.next = curr1
                curr1 = curr1.next
            node = node.next
        return head3

                