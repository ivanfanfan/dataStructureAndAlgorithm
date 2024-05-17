"""
types of queue
    1. simple queue
    2. Double-ended queue (Deque)
    3. Circular queue
    4. priority queue

basic operations in queue
    1. enqueue
    2. dequeue
    3. peek or front
    4. rear
    5. isFull
    6. isEmpty
"""


# function to add an item to the queue
# it changes rear and size
class Queue:
    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity
    #   0 1 2 3 4   capacity = 5
    #   f       r

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear+1)%(self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to queue" %str(item))

    def Dequeue(self):
        if self.isEmpty():
            print("Empty")
            return
        print("% s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",self.Q[self.rear])

if __name__ == '__main__':
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.Dequeue()
    queue.que_front()
    queue.que_rear()

