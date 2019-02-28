class Queue:
    # get empty list as queue and nothing to return
    def __init__(self):
        self.item = []
    # isEmpty() return true 
    def isEmpty(self):
        return self.item == []
    # enqueu() insert item in the pos 0
    def enqueue(self, item):
        self.item.insert(0, item)
    # dequeue() pop item and return item
    def dequeue(self):
        return self.item.pop()
    # size() get the len and return 
    def size(self):
        return len(self.item)

'''
q = Queue()
print(q.isEmpty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.item)
print(q.dequeue())
print(q.size())
print(q.isEmpty())
'''