from linked_lists.node import Node

class SinglyLinkedList:
    def __init__(self):
        self._head: Node = None
    
    def append(self, data):
        current = self._head
        if current is None:
            self._head = Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(Node(data))
    
    def insert_in_front(self, data):
        old_head = self._head
        self._head = Node(data, old_head)
    
    def _search(self, target):
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            else:
                current = current.next()
        return None
    
    def _search_recursive(self, node, target):
        if node is None:
            current = self._head
        else:
            current = node 
        if current.data() == target:
            return current
        elif current.next() is None:
            return None
        else:
            self.search_recursive(current.next(), target)
    
    def delete(self, target):
        pass
            