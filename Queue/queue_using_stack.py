class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    # Checks the stack is empty or not 
    def isempty(self):
        return self.top == None
    
    # Insert the element in the stack from top
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # Display the whole stack
    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    # Shows the top element of stack
    def peek(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            return self.top.data

    # Remove one element from the top of stack  
    def pop(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            data = self.top.data
            self.top = self.top.next
            return data
        
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self,item):
        self.s1.push(item)

    def dequeue(self):

        if self.s2.isempty() and self.s1.isempty():
            return "Queue is emmpty"
        if self.s2.isempty():
            while not self.s1.isempty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())