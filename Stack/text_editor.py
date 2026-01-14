from stack import Stack

def text_editor(text, pattern):

    u = Stack()
    r = Stack()

    for i in text:
        u.push(i)

    for i in pattern:
        if i == 'u':
            # data = u.pop()
            r.push(u.pop())
        else:
            # data = r.pop()
            u.push(r.pop())

    # Display the end result in forward order
    res = ""
    while(not u.isempty()):
        res = u.pop() + res 
    print(res)
  
text_editor("Hello", "uuur")