class DynamicStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop from an empty stack.")
            return None

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = DynamicStack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Is the stack empty?", stack.is_empty())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Is the stack empty after popping an item?", stack.is_empty())