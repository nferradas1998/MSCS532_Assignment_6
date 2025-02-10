class MyStack:
    def __init__(stack): # Using __init__ function for automatic invocation
        stack.data = []
        stack.size = 0

    def insert(stack, value):
        stack.data += [value]
        stack.size += 1

    def delete(stack): ## delete the top element from the stack
        if stack.size == 0:
            print("Stack is empty there is nothing to delete")
            return None
        value = stack.data[stack.size - 1]
        stack.data = stack.data[:stack.size - 1]
        stack.size -= 1
        return value

    def find(stack, value):
        for i in range(stack.size):
            if stack.data[i] == value:
                return i
        return -1
