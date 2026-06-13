class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        self.stack.append(val)
        print(f"Pushed: {val}| Stack : {self.stack}")

    def pop(self):
        if self.isEmpty():
            return "Stack underflow"
        val1=self.stack.pop()
        print(f"Popped : {val1} | stack: {self.stack}")
        return val1
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def display(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("TOP -> ",self.stack[::-1])

s=Stack()
s.push(10); s.push(20); s.push(30)
print("Peek: ",s.peek())
s.pop()
print("Size: ",s.size())
s.display()
s.pop()
s.pop()

