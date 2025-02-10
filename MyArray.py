class MyArray:
    def __init__(arr): ## using __init__ method for automatic invocation
        arr.data = []

    def insert(arr, value): # Add value to the next available index
        arr.data.append(value)

    def delete(arr, value): # Delete value if found in the array
        arr.data.remove(value)

    def find(array, value): ## find value, if not found then return None
        try:
            return array.data.index(value)
        except ValueError:
            return None

