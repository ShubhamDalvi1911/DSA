'''
Created a Stack 
1) Push
2) Pop
3) Peek
4) Isempty
5) Size
6) Traverse
'''
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

    # Give the size of stack
    def __len__(self):
        temp = self.top
        counter = 0
        while temp != None:
            counter = counter + 1
            temp = temp.next
        return counter

def main():
    s = Stack()
    empty = s.isempty()
    print("Before push ",empty)
    s.push(10)
    empty = s.isempty()
    print("After Push",empty)
    s.push(4)
    s.push(55)
    s.push(5)
    s.push(50)
    print("All Stack items : ")
    s.traverse()
    print("Top item of stack : ",s.peek())
    s.pop()
    print("Top item of stack : ",s.peek())
    s.pop()
    print("Top item of stack : ",s.peek())
    print(len(s))

if __name__ == "__main__":
    main()