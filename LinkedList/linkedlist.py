'''
Creat Linked List
1) Node
2) Linked List
3)Len
4) Insert at head
5) Print the linked list
6) Insert at tail
7) Insert at Middle
8) Clear
9) Delete at head
10) Delete at tail
11) Delete by value
12) Search by value
13) Delete by index
14) Search by index'''
class Node:
# Initialize the node with data and next pointer
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    # Initialize the linked list
    def __init__(self):
        # Empty list has head as None and size 0
        self.head = None
        self.n = 0

    # Return the size of the linked list
    def __len__(self):
        # Return the size of the linked list
        return self.n

    # Insert a new node at the head of the linked list
    def insert_head(self, value):
        # new node
        new_node = Node(value)

        # Create connnection
        new_node.next = self.head

        # Reassign head
        self.head = new_node

        # Increment size
        self.n = self.n + 1

    # Traverse the linked list and print each node's data
    def __str__(self):
        # Start from head
        current = self.head
        result = ''

        while current != None:
            result = result + str(current.data) + ' -> '
            current = current.next

        return result[:-3]  # Remove the last arrow
    
    # Append a new node at the end of the linked list
    def append(self, value):
        # Create new node
        new_node = Node(value)
        # If list is empty, new node becomes head
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return #early return
        
        #start from head
        current = self.head
        #traverse to the end if list is not empty
        while current.next != None:
            current = current.next

        #you are at the last node
        current.next = new_node
        self.n = self.n + 1

    # Insert a new node after a specific value
    def insert_after(self, after, value):
        # Create new node
        new_node = Node(value)
        # Start from head
        current = self.head
        # Traverse to find the after value
        while current != None:
            if current.data == after:
                break
            current = current.next

        # Case 1: after value you got = current is not None
        if current != None:
            new_node.next = current.next
            current.next = new_node
            # Increment size
            self.n = self.n + 1
         # Case 2: after value you did not get = current is None
        else:
            return "Value not found"

    # Clear the linked list    
    def clear(self):
        # Clear the linked list
        self.head = None
        # Reset size
        self.n = 0

    # Remove the head node
    def delete_head(self):
        # If list is empty, nothing to delete
        if self.head == None:
            return "List is empty"
        self.head = self.head.next
        self.n = self.n - 1

    # Remove the last node
    def pop(self):
        current = self.head
        # If list is empty, nothing to delete
        if current == None:
            return "List is empty"
        # If list has only one node
        if current.next == None:
            self.head = None
            self.n = self.n - 1
            return
        # Traverse to the second last node
        while current.next.next != None:
            current = current.next

        # You are at the second last node
        current.next = None
        self.n = self.n - 1

    # Remove a node by value
    def remove(self, value):
        current = self.head
        # If list is empty
        if self.head == None:
            return "List is empty"
        
        # If the head node is to be deleted
        if self.head.data == value:
            return self.delete_head()
        
        # Traverse to find the node to delete
        while current.next != None:
            if current.next.data == value:
                break
            current = current.next

        # If the value was found
        if current.next != None:
            current.next = current.next.next
            self.n = self.n - 1
        else:
            return "Value not found"

    # Search for an item and return its position
    def search(self, item):
        current = self.head
        pos = 0
        # Traverse the list to find the item
        while current != None:
            if current.data == item:
                return pos
            current = current.next
            pos = pos + 1

        return 'Not found in the list'
    
    # Get item by index using magic method __getitem__
    def __getitem__(self, index):
        current = self.head
        pos = 0
        # Traverse to the index
        while current != None:
            if pos == index:
                return current.data
            current = current.next
            pos = pos + 1
        return 'Index out of bounds'
    
a = Node(1)
print(a)        # Output: <__main__.Node object at ...>
print(a.data)  # Output: 1
print(a.next)  # Output: None

L = LinkedList()
print(L)        # Output: <__main__.LinkedList object at ...>
print(len(L))  # Output: 0

L.insert_head(10)
L.insert_head(20)
L.insert_head(30)
L.insert_head(40)

print(len(L))  # Output: 4

print(L)        # Output: 40 -> 30 -> 20 -> 10

L.append(50)
print(L)        # Output: 40 -> 30 -> 20 -> 10 -> 50

L.insert_after(20, 25)
print(L)        # Output: 40 -> 30 -> 20 -> 25 -> 10 -> 50

# L.clear()
print(L)        # Output:
print(len(L))  # Output: 0

L.delete_head()
print(L)        # Output: 30 -> 20 -> 25 -> 10 -> 50

L.pop()
print(L)        # Output: 30 -> 20 -> 25 -> 10

L.remove(25)
print(L)        # Output: 30 -> 20 -> 10

L.remove(30)
print(L)        # Output: 20 -> 10

L.remove(100)  # Value not found

print(L.search(10))  # Output: 1
print(L.search(100))  # Output: Not found in the list

print(L[0])  # Output: 20
print(L[1])  # Output: 10
print(L[2])  # Output: Index out of bounds