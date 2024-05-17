"""
front: get the front item from the queue
rear: get the rear item from the queue
enQueue: the new element is always inserted at the rear position
    1. check whether the queue is full
    2. if it is full then display Queue is full.
    3. if it is not full then, insert an element at the end of the queue.
deQueue: deleted from the front position
    1. check whether the queue is empty
    2. if it is empty then display Queue is empty.
    3. if it is not empty, then get the last element from and remove it from the queue.

implement circular queue using Array:
    1. Initialize an array queue of size n, where n is the maximum number of elements
        that the queue can hold.
    2. Initialize two variables front and rear to -1.
    3. Enqueue: To enqueue an element x into the queue
        1. Increment rear by 1
            If rear is equal to n, set rear to 0.
        2. if front is -1, set front to 0.

application
    1. memory management
    2. traffic system
    3. cpu scheduling
"""
class CircularQueue:

    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self,data):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is full\n")

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):
            print("Queue is empty\n")

        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front +1)% self.size
            return temp

    def display(self):
        if(self.front == -1):
            print("Queue is empty\n")
        elif (self.rear >= self.front):
            print("Elements in the circular queue are: \n",end= " ")
            for i in range(self.front, self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("Elements in the circular queue are: \n", end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i],end=" ")
            for i in range(0, self.rear+1):
                print(self.queue[i],end=" ")
            print()

        if (self.rear + 1)% self.size == self.front:
            print("Queue is full\n")


if __name__ == '__main__':
    ob = CircularQueue(5)
    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)
    ob.display()
    print("Deleted value = ", ob.dequeue())
    print("Deleted value = ", ob.dequeue())
    ob.display()
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    ob.display()






















