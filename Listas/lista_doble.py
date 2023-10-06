# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Doblemente Enlazada 
# ===========================================

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insertHead(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insertEnd(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        
    def insertBefore(self, x, data):
        if self.head is None:
            print("Lista vacía")
            return
        else:
            n = self.head
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("Item no encontrado")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
                
    def insertAfter(self, x, data):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
    
    def print(self):
        if self.head is None:
            print("Lista Vacía")
            return
        else:
            n = self.head
            while n is not None:
                print(n.item , " ")
                n = n.next
                
    def deleteFirst(self):
        if self.head is None:
            print("Lista vacía")
            return 
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None;
    
    def deleteEnd(self):
        if self.head is None:
            print("Lista vacía")
            return 
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
        
    def deleteValue(self, x):
        if self.head is None:
            print("Lista vacía")
            return 
        if self.head.next is None:
            if self.head.item == x:
                self.head = None
            else:
                print("Elemento no encontrado")
            return 

        if self.head.item == x:
            self.head = self.head.next
            self.head.prev = None
            return

        n = self.head
        while n.next is not None:
            if n.item == x:
                break;
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.item == x:
                n.prev.next = None
            else:
                print("Elemento no encontrado")
    