# Stack implementation in Python

class Stack:
    # Init function
    def __init__(self):
        self.stack = []

    # Add function
    def push(self, data):
        # check if data is already in the stack
        # if not, append data
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    # Remove function
    def pop(self):
        # check if stack is empty before removing
        if len(self.stack) <=0: 
            return("Stack is empty")
        return self.stack.pop()

    # Get the size of the stack
    def stack_size(self):
        return len(self.stack)

    # Peek function
    def peek(self):
        if self.stack == []:
            return None
        return self.stack[-1]#.pop(0) #[-1]

# Driver code
if __name__ == '__main__':

    s = Stack()
    print("Adding 89 to the stack", s.push(89))
    print("Adding 70 to the stack", s.push(70))
    print("Adding 99 to the stack", s.push(99))
    # Get the current size of the stack
    print("The size of the stack is", s.stack_size())
    # Remove elements from the stack
    print("Removing", s.pop(), "from the stack")
    print("Removing", s.pop(), "from the stack")
    # Peek next element in the stack
    print("Next element in the stack is", s.peek())
    # Get the current size of the stack after 
    # removing elements
    print("Now, the size of the stack is", s.stack_size())
