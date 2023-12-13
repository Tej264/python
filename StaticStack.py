class StaticStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top < self.capacity - 1:
            self.top += 1
            self.stack[self.top] = item
            print(f"Pushed {item} onto the stack.")
        else:
            print("Stack Overflow. Cannot push onto a full stack.")

    def pop(self):
        if self.top >= 0:
            popped_item = self.stack[self.top]
            self.top -= 1
            print(f"Popped {popped_item} from the stack.")
            return popped_item
        else:
            print("Stack Underflow. Cannot pop from an empty stack.")
            return None

    def isEmpty(self):
        return self.top == -1

stack_capacity = 5
stack = StaticStack(stack_capacity)

print("Is the stack empty?", stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)

print("Is the stack empty?", stack.isEmpty())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Is the stack empty?", stack.isEmpty())
