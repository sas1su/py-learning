class Stack:
    # contructor, initiate empty list
    def __init__(self):
        self.item = []

    # isEmpty()
    def isEmpty(self):
        return self.item == []
    # push
    def push(self, item):
        return self.item.append(item)
    # pop
    def pop(self):
        return self.item.pop()
    # peek, last element
    def peek(self):
        return self.item[-1]
    # size
    def size(self):
        return len(self.item)
'''
s = Stack()
print(s.isEmpty())
print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.pop())
print(s.peek())
print(s.size())
'''