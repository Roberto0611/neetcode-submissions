# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # edge cases
        if lists == []:
            return None
        
        # funcion para fusionar 2 listas
        def mergeLists(list1, list2):
            head = ListNode() # dummy
            currHead = head
            curr1 = list1
            curr2 = list2

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    currHead.next = curr1
                    currHead = currHead.next
                    curr1 = curr1.next
                    continue

                if curr1.val > curr2.val:
                    currHead.next = curr2
                    currHead = currHead.next
                    curr2 = curr2.next
            
            # agregar las que quedaron faltante
            if curr1:
                currHead.next = curr1 
            if curr2:
                currHead.next = curr2
                    
            return head.next
        
        # ahora debemos ir fusionando las listas en pares 
        while len(lists) > 1:
            mergeList = []

            for i in range(0,len(lists),2):
                # primero asignamos L1 y L2
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None

                # fusionamos y agregamos a la lista
                mergeList.append(mergeLists(l1,l2))

            # actualizamos la lista
            lists = mergeList

        return lists[0]
