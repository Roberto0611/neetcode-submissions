# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = ListNode()
        curr1 = l1
        curr2 = l2
        carry = 0
        prevNode = resultHead

        while curr1 or curr2 or carry:
            # limpiar nulls
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            # sumar 
            sumInt = v1 + v2 + carry
            carry = 0

            if sumInt >= 10:
                sumInt = sumInt - 10
                carry = 1
            
            newNode = ListNode(sumInt)
            prevNode.next = newNode

            prevNode = newNode

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return resultHead.next