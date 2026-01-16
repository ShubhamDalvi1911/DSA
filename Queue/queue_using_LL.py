class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            return "Empty"
        else:
            self.front = self.front.next

    def is_empty(self):
        return self.front == None
    
    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            counter += 1
            temp = temp.next
        return counter

    def front_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.front.data
        
    def rear_item(self):
        if self.rear == None:
            return "Empty"
        else:
            return self.rear.data

    def traverse(self):
        temp = self.front
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next


q = Queue()

q.enqueue(5)
q.enqueue(4)
q.enqueue(6)

q.traverse()

print(q.is_empty())

print(q.front_item())
print(q.rear_item())

q.dequeue()
q.dequeue()
q.traverse()
q.dequeue()
print(q.size())
print(q.traverse())