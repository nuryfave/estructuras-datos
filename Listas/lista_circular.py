# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Circular Simplemente Enlazada 
# ===========================================

class Node(): # Clase Nodo General
    # Constructor
    def __init__(self , data: str):
        super().__init__()
        self.data  = data
        self.next = None
        self.prev = None
    
class CircularList(): # Clase Lista Circular

    # Constructor
    def __init__(self): 
        self.head = None
    
    # Lista Vacía   
    def is_empty(self): 
        if self.head is None :
            print("Lista Vacía")
    
    # Longitud de la Lista
    def length(self):     
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            if cur.next == self.head:
                break
            else:
                cur = cur.next
        return count
    
    # Imprimir la lista
    def printList(self): 
        if self.is_empty():
            return
        cur = self.head
        print(cur.data)
        while cur.next != self.head:
            cur = cur.next
            print(cur.data)
    
    # Agregar nodo cabeza
    def addFirst(self, data): 
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head
            self.head = node 
    
    # Agregar nodo final
    def addLast(self, data): 
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head
    
    # Agregar nodo en una posición
    def addInPosition(self, index, data):
        node = Node(data)
        if index < 0 or index > self.length():
            print ("Posición de inserción incorrecta")
            return False
        elif index == 0:
            self.add_first(data)
        elif index == 0:
            self.add_last()
        else:
            cur = self.head
            pre = Ninguno 
            count = 0
            while count < index:
                pre = cur
                cur = cur.next
                count += 1
            pre.next = node
            node.next = cur
    
    # Eliminar nodo indicado
    def remove(self, data):
        if self.is_empty():
            return
        elif data == self.head.data:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            pre = None
            while cur.data != data:
                pre = cur
                cur = cur.next
            pre.next = cur.next
    
    # Buscar Nodo
    def search(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            elif cur.next == self.head:
                return False
            else:
                cur = cur.next
        return False