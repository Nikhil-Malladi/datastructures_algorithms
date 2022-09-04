# Queue
class Queue(object):
    def __init__(self):
        self.queue=[]

    def insertElement(self,element):
        self.queue.append(element)
        return self.queue

    def removeElement(self):
        if not len(self.queue):
            return None
        return self.queue.pop()

    def printQueue(self):
        print(self.queue)

Q=Queue()
Q.insertElement(2)
Q.insertElement(4)
Q.insertElement(6)

print("after inserting queue",Q.printQueue())

Q.removeElement()
Q.removeElement()

print("after removing queue",Q.printQueue())
