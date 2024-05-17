
class PriorityQueueNode:

    def __init__(self, value, priority):
        self.data = value
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def isEmpty(self):
        return True if self.front == None else False

    def push(self,value,priority):
        # empty
        if self.isEmpty() == True:
            self.front = PriorityQueueNode(value,priority)
            return 1
        # not empty
        else:
            # the priority of first is less than inserted element
            if self.front.priority < priority:
                newNode = PriorityQueueNode(value,priority)
                newNode.next = self.front
                self.front = newNode
                return 1
            # the priority of first is greater than inserted
            #  10 -> 9 -> 8 -> 7
            #   f                    inserted 6
            else:
                temp = self.front
                # use  temp.next to compare
                # temp used to remember previous node
                while temp.next:
                    if priority > temp.next.priority:
                        break
                    temp = temp.next

                newNode = PriorityQueueNode(value,priority)
                newNode.next = temp.next
                temp.next = newNode
                return 1

    def pop(self):

        if self.isEmpty() == True:
            return
        else:
            self.front = self.front.next
            return -1

    def peek(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front.data

    def traverse(self):
        if self.isEmpty() == True:
            return "Queue is Empty"
        else:
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

if __name__ == '__main__':
    # Creating an instance of Priority
    # Queue, and adding values
    pq = PriorityQueue()
    pq.push(4, 1)
    pq.push(5, 2)
    pq.push(6, 3)
    pq.push(7, 0)
    # 7 4 5 6
    # Traversing through Priority Queue
    pq.traverse()

    # Removing highest Priority item
    # for priority queue
    pq.pop()
    print("--------------\n")
    pq.traverse()
































