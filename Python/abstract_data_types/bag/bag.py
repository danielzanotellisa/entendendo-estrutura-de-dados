from linked_lists.simple_linked_list import SinglyLinkedList

class Bag:
    def __init__(self):
        self._data = SinglyLinkedList()
    
    def insert(self, data):
        self._data.insert_in_front(data)
    
    def traverse(self):
        return self._data.traverse(print)