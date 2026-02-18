from node import Node

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
        current = self._head
        previous = None
        
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        raise ValueError("Target not in the list")
    
    def delete_from_front(self):
        current_head = self._head
        if current_head is None:
            raise ValueError("The list is empty")
        
        new_head = current_head.next()
        
        if new_head is None:
            self._head = None
            return current_head.data()
        else:
            self._head = new_head
            return current_head.data()
    
    def traverse(self, callback):
        current = self._head
        
        if current is None:
            raise ValueError("The list is empty")
        
        while current is not None:
            callback(current.data())
            current = current.next()

def main():
    list = SinglyLinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    
    list.traverse(print)
    
    list.delete_from_front()
    print('\n')
    list.traverse(print)
    
if __name__ == '__main__':
    main()
            