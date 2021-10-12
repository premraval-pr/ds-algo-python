# FIFO Structure: First In First Out

class Queue:

    def __init__(self):
        self.queue = []

    # Insert the data at the end / O(1)
    def enqueue(self, data):
        self.queue.append(data)

    # remove and return the first item in queue / O(n) Linear time complexity
    def dequeue(self):
        if self.is_empty():
            return -1
        data = self.queue[0]
        del self.queue[0]
        return data

    # returns the first element / O(1)
    def peek(self):
        return self.queue[0]

    # check if the queue is empty / O(1)
    def is_empty(self):
        return self.queue == []

    # returns the size / O(1)
    def queue_size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dequeue: %d" % queue.dequeue())
print("Size: %d" % queue.queue_size())
print("Peek: %d" % queue.peek())
print("Size: %d" % queue.queue_size())
print("Dequeue: %d" % queue.dequeue())
print("Dequeue: %d" % queue.dequeue())
print("Dequeue: %d" % queue.dequeue())
