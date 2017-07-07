class PriorityQueue:
    """
    Array-based priority queue implementation.
    """

    def __init__(self):
        """
        Initially empty priority queue.
        """
        self.queue = []
        self.min_index = 0
        self.length = 0

    def __len__(self):
        # Number of elements in the queue.
        return self.length

    def __str__(self):
        return " ".join(str(x) for x in self.queue[0:len(self)])

    def parent(self, i):
        return (i - 1)/2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < len(self) and self.queue[l] < self.queue[i]:
            smallest = l
        else:
            smallest = i
        if r < len(self) and self.queue[r] < self.queue[smallest]:
            smallest = r
        if smallest != i:
            temp = self.queue[i]
            self.queue[i] = self.queue[smallest]
            self.queue[smallest] = temp
            self.minHeapify(smallest)

    def heapIncreaseKey(self, i, key):
        if key > self.queue[i]:
            raise ValueError('new key is larger than current key')
        self.queue[i] = key
        while i > 0 and self.queue[self.parent(i)] > self.queue[i]:
            temp = self.queue[i]
            self.queue[i] = self.queue[self.parent(i)]
            self.queue[self.parent(i)] = temp
            i = self.parent(i)

    def append(self, key):
        self.length += 1
        if len(self) > len(self.queue):
            self.queue.append(float('inf'))
        else:
            self.queue[len(self) - 1] = float('inf')
        self.heapIncreaseKey(len(self) - 1, key)


    def makeMinHeap(self):
        i = len(self)/2
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def _find_min(self):
        return self.min_index

    def pop(self):
        """
        Removes the minimum element in the queue.

        Returns:
            The value of the removed element.
        """
        if len(self) == 0:
            return ValueError("Heap underflow")
        min = self.queue[self.min_index]
        self.queue[self.min_index] = self.queue[len(self) - 1]
        self.length -= 1
        self.minHeapify(0)
        return min

    def min(self):
        """
        The smallest element in the queue.
        """
        if len(self) == 0:
            return None
        return self.queue[self.min_index]

    def isMinHeap(self):
        result = True
        i = 0
        while self.left(i) < len(self):
            l = self.left(i)
            r = self.right(i)
            if l < len(self) and self.queue[l] < self.queue[i]:
                result = False
            if r < len(self) and self.queue[r] < self.queue[i]:
                result = False
            i += 1
        return result

import random
randomInts = [random.randint(0,1000) for r in xrange(10)]
q = PriorityQueue()
for r in randomInts:
    print("Appended: " + str(r))
    q.append(r)
    print("After append: " + str(q))
    # print("Length heap: " + str(len(q)))
    # print("Length queue: " + str(len(q.queue)))
    print("Is minHeap: " + str(q.isMinHeap()))


for i in xrange(2):
    print("After popped: " + str(q))
    # print("Length heap: " + str(len(q)))
    # print("Length queue: " + str(len(q.queue)))
    print("Is minHeap: " + str(q.isMinHeap()))

randomInts = [random.randint(0, 1000) for r in xrange(5)]
for r in randomInts:
    print("Appended: " + str(r))
    q.append(r)
    print("After append: " + str(q))
    # print("Length heap: " + str(len(q)))
    # print("Length queue : " + str(len(q.queue)))
    print("Is minHeap: " + str(q.isMinHeap()))

