class Stack:
        def __init__(self):
                self.items = []
        
        def is_empty(self):
                return self.items == []
        
        def push(self, value):
                return self.items.append(value)
        
        def pop(self):
                return self.items.pop()
        
        def peek(self):
                last = len(self.items) - 1
                return self.items[last]
        
        def size(self):
                return len(self.items)
        


value = Stack()
# value.push(1)
# value.push(2)
# value.push(20)
# value.pop()
# print(value.peek())
# print(value.size())
# print(value.is_empty())

helloStr = 'hello'.strip()
for i, c in enumerate(helloStr):
        print(i, helloStr[i])
        value.push(c)


reverse = ''

for h in helloStr:
        reverse += value.pop()


print(reverse)



