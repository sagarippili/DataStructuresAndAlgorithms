class Stack():
    def __init__(self, stackSize):
        self._top = -1
        self._stackSize = stackSize
        self._stackArray = [None] * stackSize

    def getStackSize(self):
        return (self._stackSize)

    def setStackSize(self, stackSize):
        self._stackSize = stackSize

    def isEmpty(self):
        return True if self._top == -1 else False

    def isFull(self):
        return True if self._top == self.getStackSize() -1 else False

    def push(self, pushedElement):
        if self.isFull():
            print ('The Stack is already Full. Cannot push anymore elements')
        else:
            self._top += 1
            self._stackArray[self._top] = pushedElement

    def pop(self):
        if not(self.isEmpty()):
            poppedElement = self._stackArray[self._top]
            self._stackArray[self._top] = None
            self._top -= 1
            return poppedElement
        else:
            print ('The stack is already empty. Nothing to pop')

    def peek(self):
        return self._stackArray[self._top]