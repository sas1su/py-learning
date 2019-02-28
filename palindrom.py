from dequeue import Dequeue

def palChecker(word):
    dq = Dequeue()
    for char in word:
        dq.addRear(char)

    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            return False
        
    return True

print(palChecker('radar'))
print(palChecker('radarr'))
print(palChecker('tot'))