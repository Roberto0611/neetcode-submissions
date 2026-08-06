class ListNode:
    def __init__(self,val=0,key=None,prev = None,next = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def remove(self, node):
        # 1. Identificamos a los vecinos del nodo a borrar
        vecino_izq = node.prev
        vecino_der = node.next
        
        # 2. Los conectamos entre sí, puenteando y aislando a nuestro nodo
        vecino_izq.next = vecino_der
        vecino_der.prev = vecino_izq

    def insert(self, node):
        # 1. Identificamos al nodo que actualmente está al final (antes del rigth)
        vecino_izq = self.rigth.prev
        
        # 2. Conectamos nuestro nodo al vecino izquierdo
        vecino_izq.next = node
        node.prev = vecino_izq
        
        # 3. Conectamos nuestro nodo al rigth (el final de la lista)
        node.next = self.rigth
        self.rigth.prev = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}
        self.left = None
        self.ritgh = None

        # crear nodo left
        self.left = ListNode()
        
        # crear nodo rigth
        self.rigth = ListNode()

        # enlazar nodos
        self.rigth.prev = self.left
        self.left.next = self.rigth

    def get(self, key: int) -> int:
        node = self.nodeMap.get(key,-1)

        if node == -1:
            return -1 
        
        # actualizar punteros
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        
        # si ya existia este nodo lo borramos
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])

        # agregar el nuevo al nodo y al mapa
        newNode = ListNode(value, key=key)
        self.nodeMap[key] = newNode
        self.insert(newNode)

        if len(self.nodeMap) > self.capacity:
            # eliminamos el ultimo
            delKey = self.left.next.key
            self.remove(self.left.next)

            del self.nodeMap[delKey]
