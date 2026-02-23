from double_node import DoubleNode

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def insert_in_front(self,data):
        if self._head is None:
            self._head = self._tail = DoubleNode(data)
        else:
            old_head = self._head
            self._head = DoubleNode(data)
            self._head.append(old_head)
            
    def insert_to_back(self, data):
        if self._tail is None:
            self._tail = self._head = DoubleNode(data)
        else:
            old_tail = self._tail
            self._tail = DoubleNode(data)
            self._tail.prepend(old_tail)
    