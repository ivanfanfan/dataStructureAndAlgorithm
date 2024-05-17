class MaxHeap:
    # A pointer pointing to the elements
    # in the array in the heap
    arr = []
    # Maximum possible size of the max heap
    maxSize = 0

    heapSize = 0

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None] * maxSize  # todo what mean?
        self.heapSize = 0

    # heapify a sub-tree taking the given index as the root
    def MaxHeapify(self, i):
        l = self.lChild(i)
        r = self.rChild(i)
        largest = i
        if l < self.heapSize and self.arr[l] > self.arr[i]:
            largest = l
        if r < self.heapSize and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.MaxHeapify(largest)  # recursion

    def parent(self, i):
        return (i - 1) // 2


    def lChild(self, i):
        return (2 * i + 1)

    def rChild(self, i ):
        return (2 * i + 2)

    def removeMax(self):
        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return self.arr[0]

        root = self.arr[0]
        self.arr[0] = self.arr[self.heapSize - 1]
        self.heapSize -= 1

        self.MaxHeapify(0)

        return root

    # increases values of key at index 'i' to new_val.
    def increaseKey(self, i , newVal):
        self.arr[i] = newVal
        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)

    def getMax(self):
        return self.arr[0]

    def curSize(self):
        return self.heapSize

    def deleteKey(self, i):
        # It increases the value of key to infinity and then
        # removes the maximum value
        self.increaseKey(i, float("inf"))
        self.removeMax()

    def insertKey(self, x):
        # to check whether the key can be inserted or not
        if self.heapSize == self.maxSize:
            print("\n Overflow : could not insertKey \n")
            return
        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = x

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = temp
            i = self.parent(i)


# Driver
if __name__ == '__main__':

    h = MaxHeap(15)
    k, i, n = 6, 0, 6
    print("Entered 6 keys: -3, 10, 12, 8, 2, 14 \n")
    h.insertKey(3)
    h.insertKey(10)
    h.insertKey(12)
    h.insertKey(8)
    h.insertKey(2)
    h.insertKey(14)
    # printing the current size of the heap
    print(f"The current size of the heap is {str(h.curSize())}" + "\n")

    print("The current maximum element is "+ str(h.getMax()))

    # delete key at index 2
    h.deleteKey(2)

    # printing the size of the heap after deletion

    print("The current size of the heap is "+ str(h.curSize())+"\n")

    # Inserting 2 new keys into the heap

    h.insertKey(15)
    h.insertKey(5)

    print("The current size of the heap is "+ str(h.curSize())+"\n")
    print("The current maximum element is "+ str(h.getMax())+ "\n")








































