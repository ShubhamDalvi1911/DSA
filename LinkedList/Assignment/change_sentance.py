'''Given a linked list of characters. Write a python function to return a new string 
that is created by appending all the characters given in the linked list as per the
rule given below
    Replace * or / by a single space
    In case of two consecutive occurance of * or / repalce these two occurance by a 
    single space and convert the next character to upper case'''

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
    
    def traverse(self):
        # Start from head
        current = self.head
        result = ''

        while current != None:
            result = result + str(current.data) 
            current = current.next

        print(result)

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
    
    def change_sent(self):
        temp = self.head

        while temp != None:
            if temp.data == '*' or temp.data == '/':
                temp.data = ' '
                if temp.next.data == '*' or temp.next.data == '/':
                    temp.next.next.data = temp.next.next.data.upper()
                    temp.next = temp.next.next
 
            temp = temp.next


word_list = LinkedList()
word_list.append("T")
word_list.append("h")
word_list.append("e")
word_list.append("/")
word_list.append("*")
word_list.append("s")
word_list.append("k")
word_list.append("y")
word_list.append("*")
word_list.append("i")
word_list.append("s")
word_list.append("/")
word_list.append("/")
word_list.append("b")
word_list.append("l")
word_list.append("u")
word_list.append("e")

word_list.change_sent()
word_list.traverse()