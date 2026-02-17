from arrays.core import Array

class DynamicArray:
    def __init__(self, initial_capacity = 1, typecode = 'l'):
        self._array = Array(initial_capacity, typecode)
        self._size = 0
        self._capacity = initial_capacity
        self._typecode = typecode
        
    def _double_size(self):
        old_array = self._array
        self._array = Array(self._capacity * 2, self._typecode)
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]
    
    def insert(self, entry):
        if self._size >= self._capacity:
            self._double_size()
        self._array[self._size] = entry
        self._size += 1
    
    def find(self, target):
        for i in range(self._size):
            if self._array[i] == target:
                return i
        return None
    
    def delete(self, target):
        index = self.find(target)
        
        if index is None:
            raise ValueError("Target could not be found in the array")
        
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
        
        if self._capacity > 1 and self._size <= self._capacity/4:
            self._halve_size()
    
    def _halve_size(self):
        old_array = self._array
        self._array = Array(self._capacity / 2, self._typecode)
        for i in range(self._size):
            self._array[i] = old_array[i]    
        
        