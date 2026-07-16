# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ## Mi tercer approach es este
        # el anterior era eficiente, pero ahora necesitamos mejorar en memoria
        # intentare sin usar ninguna estructura....
        isLoop = False
        fasthead = head

        while head and fasthead:
            # mover la head rapida, 2 posiciones
            fasthead = fasthead.next
            if fasthead:
                fasthead = fasthead.next
            else:
                # si es nulo singifica que hay final
                break

            # mover la head lenta
            head = head.next

            # si estan en la misma posicion es que hay un loop
            if head == fasthead:
                isLoop = True
                break

        return isLoop