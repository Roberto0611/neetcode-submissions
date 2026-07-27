# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1.- lo primero que hacemos es encontrar el nodo de en medio
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next 
            fast = fast.next 
        
        # 2.- ahora cortamos los nodos y reverseamos la segunda lista
        curr = slow
        prev = None

        while curr:
            # guardar y actualizar next
            nextNode = curr.next
            curr.next = prev

            # actualizar todo a la siguiente posicion
            prev = curr
            curr = nextNode
            
        # Nuestra lista al reves inicia en el prev
        revHead = prev

        # 3.- ahora debemos mezclar las dos listas
        # *lista 1 inicia en head
        # *lista 2 inicia en revHead

        curr = head

        while revHead.next:
            # actualizar head
            headNext = curr.next
            curr.next = revHead

            # actualizar rev head
            revHeadNext = revHead.next 
            revHead.next = headNext

            # actualizar punteros
            revHead = revHeadNext
            curr = headNext
