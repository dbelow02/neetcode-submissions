class KthLargest:
    #Need to revisit heap datastructure

    def __init__(self, k: int, nums: List[int]):
        #O(nlog(k+1)) time, O(k) space
        #Idea is just to keep a sorted list of k elts
        #min Heap?
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k
        while len(self.minHeap) > k:
            #Trim heap until only k elts
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #O(log(k+1)) time, O(k) space

        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            #Heap may be smaller than k (don't pop!)
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

