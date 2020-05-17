class Queue():
    def __init__(self, queueSize):
        self._front = 0
        self._rear = -1
        self._queueSize = queueSize
        self._queueArray = [None] * queueSize

    def getQueueSize(self):
        return (self._queueSize)

    def setQueueSize(self, queueSize):
        self._queueSize = queueSize

    def isEmpty(self):
       return True if self._front > self.getQueueSize() - 1 else False

    def isFull(self):
       return True if self._rear == self.getQueueSize() - 1 else False

    def enqueue(self, enqueueElement):
        if self.isFull():
            print ('The Queue is already Full. Cannot enqueue anymore elements')
        else:
            self._rear += 1
            self._queueArray[self._rear] = enqueueElement

    def dequeue(self):
        if not(self.isEmpty()):
            dequeueElement = self._queueArray[self._front]
            self._queueArray[self._front] = None
            self._front += 1
            return dequeueElement
        else:
            print ('The queue is already empty. Nothing to dequeue')

    def peek(self):
        return self._queueArray[self._front]