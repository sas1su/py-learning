from queue import Queue

# take a list of names, num
# until the num reached it will deque and immdtly enqueue
# when reached 1 name left dequeue and retur
def hotPotato(namelist, num):
    simqueue = Queue()

    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())

    return simqueue.dequeue()
        

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))