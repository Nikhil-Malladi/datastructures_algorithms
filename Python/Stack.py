# Stack
class Stack(object):
    def __init__(self):
        self.stack=[]

    def insertElement(self,element):
        return self.stack.append(element)

    def removeElement(self):
        if not len(self.stack):
            return None
        return self.stack.pop(0)

    def printStack(self):
        print(self.stack)

S=Stack()
S.insertElement(1)
S.insertElement(5)
S.insertElement(10)

print("after insertion",S.printStack())

stack=S.removeElement()
stack=S.removeElement()
print("after removing",S.printStack())
