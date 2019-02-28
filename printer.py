from queue import Queue
import random

class Printer:
    # intiate variable for printer
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    # tick() function to find remaining time
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    # busy() function to find printer free
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    # startNext() function to start a new job
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    # initiate task vars
    # keep the current timestap to calculate how much time to wait
    # number of pages for the task 1-20
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    # give the number of pages to printer class to calculate remainingtime
    def getPages(self):
        return self.pages
    # find waiting time
    def waitTime(self, currentime):
        return currentime - self.timestamp

def simulation(numSeconds, pagePerMinute):
    labprinter = Printer(pagePerMinute)
    printqueue = Queue()
    waitingtimes = []
    # give the task to printer
    # start to run for numSeconds
    for currentSecond in range(numSeconds):
        if newPrintTask:
            task = Task(currentSecond)
            printqueue.enqueue(task)
        # give task from queue if print is not busy and printqueue is not empty
        if (not labprinter.busy()) and (not printqueue.isEmpty()):
            nexttask = printqueue.dequeue()
            # keep track of waiting time
            waitingtimes.append(nexttask.waitTime(currentSecond))
            # start the task
            labprinter.startNext(nexttask)
        # check the tick to see timeremaining is 0 to start new task
        labprinter.tick()
    # find the avg waitingtime and print
    avgwaitingtime = sum(waitingtimes)/len(waitingtimes)
    print("Average wait %6.2f secs %3d tasks reamaining"% (avgwaitingtime, printqueue.size()))

def newPrintTask():
    # if the num is 180 then start a newTask can start
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(1):
    # make the printer available for 1hr 3600s, and page/m is 5
    # find how much time it has to wait for esch Task to finish
    simulation(3600, 10)