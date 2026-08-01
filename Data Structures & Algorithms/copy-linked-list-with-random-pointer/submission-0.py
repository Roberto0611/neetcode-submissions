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
        # create map
        NodeMap = dict()

        # create a copy
        curr = head
        nxt = head
        copyDummy = Node(0)
        prevCopy = copyDummy
        i = 0
        while(curr):
            # crear nodo copia
            copy = Node(curr.val)

            # si es el primero
            if i == 0:
                copyDummy.next = copy

            # guardarlo en el mapa
            NodeMap[curr] = copy

            # asignar next al previo
            if prevCopy != copyDummy:
                prevCopy.next = copy

            # actualizar prev
            prevCopy = copy 

            # next
            curr = curr.next
            i+=1 

        copyHead = copyDummy.next
        
        # asignar randoms
        curr = head
        copyCurr = copyHead
        random = None
        while(curr):
            # asignar el random a la copia usando el valor del mapa
            if curr.random == None:
                copyCurr.random = None
            else:
                copyCurr.random = NodeMap[curr.random]

            # avanzar punteros
            curr = curr.next
            copyCurr = copyCurr.next

        return copyHead

