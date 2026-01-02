import ctypes

class MereList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # Create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def append(self, item):
        if self.n == self.size:
            #resize array
            self.__resize(self.size * 2)

        # Append
        self.A[self.n] = item
        self.n = self.n + 1

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