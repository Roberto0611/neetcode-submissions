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
        prevNode = resultHead
        newNode = None
        lastNode = False
        sumInt = 0
        carry = 0

        while curr1 or curr2:
            # lastNode?
            if curr1 and curr2:
                sumInt = curr1.val + curr2.val + carry
                if curr1.next or curr2.next:
                    lastNode = False
                else:
                    lastNode = True
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                sumInt = curr1.val + carry
                if curr1.next:
                    lastNode = False
                else:
                    lastNode = True
                curr1 = curr1.next
            else:
                sumInt = curr2.val + carry
                if curr2.next:
                    lastNode = False
                else:
                    lastNode = True
                curr2 = curr2.next

            if lastNode:
                # agregar los ultimos nodos
                #//sumInt = curr1.val + curr2.val + carry
                print(f'lastNode: {sumInt} ')
                if sumInt >= 10:
                    newNode = ListNode(sumInt - 10)
                    prevNode.next = newNode
                    prevNode = newNode

                    newNode = ListNode(1)
                    prevNode.next = newNode
                    prevNode = newNode

                else:
                    newNode = ListNode(sumInt)
                    prevNode.next = newNode
                break
            
            # si no es ultimo nodo...
            #//sumInt = curr1.val + curr2.val + carry
            carry = 0

            if sumInt >= 10:
                sumInt = sumInt - 10
                carry = 1
            
            newNode = ListNode(sumInt)
            prevNode.next = newNode

            prevNode = newNode
            #curr1 = curr1.next
            #curr2 = curr2.next

        return resultHead.next