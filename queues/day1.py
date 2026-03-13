class Queue:
        def __init__(self):
                self.items = []
        
        def enqueue(self, value):
                return self.items.insert(0, value)

        def dequeue(self):
                return self.items.pop()

        def is_empty(self):
                return self.items == []
        
        def size(self):
                return len(self.items)

queue = Queue()
queue.enqueue(20)
queue.enqueue(100)
queue.dequeue()

print(queue.size())