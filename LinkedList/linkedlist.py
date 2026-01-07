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