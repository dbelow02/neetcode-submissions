class MedianFinder:

    def __init__(self):
        self.lowHeap = [] #maxheap of low nums
        self.highHeap = [] #min heap of high nums
        self.k = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowHeap, -num)
        #keeps heap low < heap high:
        heapq.heappush(self.highHeap, -heapq.heappop(self.lowHeap))
        self.k += 1
        if len(self.highHeap) - len(self.lowHeap) > 0:
            #Balance
            #Take biggest elt of lowHeap ([0]) and put in highHeap!
            #Also keeps both sorted.
            heapq.heappush(self.lowHeap, -heapq.heappop(self.highHeap))


    def findMedian(self) -> float:
        if self.k % 2 == 0:
            return (-self.lowHeap[0] + self.highHeap[0]) / 2
        else:
            return -self.lowHeap[0]
        