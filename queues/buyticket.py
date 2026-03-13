import random
import time

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
        
        def simulate_line(self, till_show, max_time):
                pq = Queue()
                tix_sold = []

                for i in range(10):
                        pq.enqueue('Person ' + str(i))

                t_end = time.time() + till_show
                now = time.time()

                while now < t_end and not pq.is_empty():
                        now = time.time()
                        r = random.randint(0, max_time)
                        time.sleep(r)
                        person = pq.dequeue()
                        tix_sold.append(person)
                return tix_sold
        


queue = Queue()
# queue.enqueue(20)
# queue.enqueue(100)
# queue.dequeue()
sold = queue.simulate_line(10, 2)
print(sold)

# print(queue.size())