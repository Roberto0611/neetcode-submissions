# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # primero vamos a invertir los primeros k nodos
        prev = None
        curr = head
        nxt = head

        for i in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        newHead = prev
        secondHead = curr

        while True:
            # si no hay nodos
            if not curr:
                break

            # contar si aun hay espacio
            valid_list = True
            start = curr
            for i in range(k):
                if not curr:
                    valid_list = False
                    break

                curr = curr.next
            
            # si la lista no es valida, conectamos los nodos 
            if not valid_list:
                head.next = start
                break
            
            # si la lista es valida
            # invertir la lista
            prev = None
            curr = start
            nxt = start

            for i in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # conectar
            head.next = prev
            head = start
            
        return newHead
