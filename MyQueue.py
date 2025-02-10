class MyQueue:
    def __init__(queue): ## Using __init__ method for automatic invocation
        queue.data = []
        queue.size = 0

    def insert(queue, value):
        queue.data += [value]
        queue.size += 1

    def delete(queue): # Will remove the front element in the queue
        if queue.size == 0:
            print("Queue is empty nothing to delete")
            return None
        value = queue.data[0]
        queue.data = queue.data[1:]
        queue.size -= 1
        return value

    def find(queue, value):
        for i in range(queue.size):
            if queue.data[i] == value:
                return i
        return -1