'''
Implementation of Dynamic Array in Python
1) Create List
2) len
3) append
4) print
5) indexing
6) pop
7) clear
8) find
9) insert
10) delete
11) remove
'''

import ctypes

class MereList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'
    
    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return IndexError("Index out of bounds")
        
    def __delitem__(self, pos):
        if 0<= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n - 1

    def append(self, item):
        if self.n == self.size:
            #resize array
            self.__resize(self.size * 2)

        # Append
        self.A[self.n] = item
        self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return IndexError("Array is empty")
        print(self.A[self.n-1])
        self.n = self.n -1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
            
        return 'valueerror not in array'
    
    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size * 2)

        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            #delete
            self.__delitem__(pos)
        else:
            return pos

    def clear(self):
        self.n = 0
        self.size = 1

    def __resize(self, new_capacity):
        # Create new array with new_capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity

        # Copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]

        # reassign A
        self.A = B

    def __make_array(self, capacity):
        # Create a C type array(static, referantial) with size capacity
        return (capacity * ctypes.py_object)()
    
L = MereList()
print(L)

L.append("Shubham")
L.append(80.36)
L.append(100)

print(len(L))
print(L)
print(L[1])
print(L[5])

L.pop()
print(L)

# L.clear()   
# print(L)

print(L.find(80.36))

L.insert(1, "Hello")
print(L)

del L[0]
print(L)

L.remove(80.36)
print(L)