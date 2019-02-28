class Dequeue:
    def __init__(self):
        self.item = []
    def addFrot(self, item):
        self.item.append(item)
    def removeFront(self):
        return self.item.pop()
    def addRear(self, item):
        self.item.insert(0, item)
    def removeRear(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)

'''
dq = Dequeue()
print(dq.isEmpty())
dq.addFrot(4)
dq.addFrot(3)
dq.addFrot(2)
dq.addFrot(1)
print(dq.removeFront())
print(dq.removeRear())
print(dq.isEmpty())
print(dq.size())
'''
