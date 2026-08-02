"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        curr = head
        copy = None

        # insertar las copias 
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy

            curr = copy.next
        
        # asignar randoms
        curr = head
        while curr:
            copy = curr.next

            if curr.random:
                copy.random = curr.random.next
            else:
                copy.random = None

            curr = copy.next

        # desenredar los nodos
        copyHead = head.next
        curr = head
        copy = curr.next

        while curr:
            curr.next = copy.next
            curr = curr.next

            if curr:
                copy.next = curr.next
                copy = copy.next
            else:
                copy.next = None

        return copyHead