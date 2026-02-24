from linked_lists.simple_linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self._data = SinglyLinkedList()
    
    def push(self,data):
        self._data.insert_in_front(data)
        
    
    def pop(self):
        self._data.delete_from_front()