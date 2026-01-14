from stack import Stack
def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)

    res = ""
    while (not s.isempty()):
        res =  res + s.pop() 
    print(res)

reverse_string("Hello")