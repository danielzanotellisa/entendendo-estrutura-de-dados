from arrays.core import Array

class UnsortedArray:
    def __init__(self, max_size, typecode = 'l'):
        self._array = Array(max_size, typecode)
        self._size = 0
        self._max_size = max_size
        
    def insert(self, entry):
        if self._size >= len(self._array):
            raise ValueError ('The array is already full')
        else:
            self._array[self._size] = entry
            self._size += 1
    
    def find(self, target):
        for i in range(0, self._size):
            if self._array[i] == target:
                return i
        return None
    
    def delete(self, target):
        if self._size == 0:
            raise ValueError('Array is empty')
        elif target < 0 or target >= self._size:
            raise ValueError('Index out of range')
        else:
            self._array[target] = self._array[self._size - 1]
            self._size -= 1
            
    def traverse(self, callback):
        for index in range(self._size):
            callback(self._array[index])
            