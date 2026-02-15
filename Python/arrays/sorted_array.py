from arrays.core import Array

class SortedArray:
    def __init__(self, max_size: int, typecoode: str = ''):
        self._array = Array(max_size, typecoode)
        self._max_size = max_size
        self._size = 0
        
    def insert(self, entry):
        if self._size >= len(self._array):
            raise ValueError('Array is already full')
        
        for index in range(self._array[self._size], 0, -1):
            if self._array[index - 1] <= entry:
                self._array[index] = entry
                self._size += 1
                return
            else:
                self._array[index] = self._array[-1]
        
        self._array[0] = entry
        self._size += 1  
    
    def search(self, target):
        if self._size == 0:
            return None
        
        for i in range(self._array):
            if self._array[i] == target:
                return i
        
        return None  
    
    def delete(self, target):
        index = self.search(target)
        if not index:
            raise ValueError('Value does not exist in array')
        
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i+1]
        self._size -= 1
    
    def traverse(self, callback):
        for i in range(self._size):
            callback(self._array[i])      