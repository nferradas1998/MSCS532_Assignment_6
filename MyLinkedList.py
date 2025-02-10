class Node: # creating node object to form the linked list
    def __init__(node, value): # Using __init__ function for automatic invocation
        node.value = value
        node.next = None

class MyLinkedList:
    def __init__(list): ## using __init__ function for automatic invocation
        list.head = None

    def insert(list, value): # insert at the end of the list (appends to final node)
        new_node = Node(value)
        if list.head is None:
            list.head = new_node
            return
        current = list.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(list, value): 
        if list.head is None:
            print("List is empty, there is nothing to delete")
            return
        if list.head.value == value:
            list.head = list.head.next
            return
        current = list.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next is None:
            print("Not found")
        else:
            current.next = current.next.next

    def traverse(list): # print all elements of the list 
        current = list.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)