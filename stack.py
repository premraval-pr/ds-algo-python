# LIFO structure Last In First Out

class Stack:

    def __init__(self):
        self.stack = []

    # Insert item / O(1)
    def push(self, data):
        self.stack.append(data)

    # Remove the top item and return / O(1)
    def pop(self):
        if self.is_empty():
            return -1
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # Returns the top item / O(1)
    def peek(self):
        return self.stack[-1]

    # checks if the stack is empty / O(1)
    def is_empty(self):
        return self.stack == []

    # return the size / O(1)
    def stack_size(self):
        return len(self.stack)


st = Stack()
st.push(1)
st.push(2)
st.push(3)
print("Size: %d" % st.stack_size())
print("Popped: %d" % st.pop())
print("Size: %d" % st.stack_size())
print("Peek: %d" % st.peek())
print("Size: %d" % st.stack_size())
print("Popped: %d" % st.pop())
print("Popped: %d" % st.pop())
print("Popped: %d" % st.pop())
