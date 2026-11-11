class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Is this not just a max heap, then pop k times?
        #firstly heap.
        minHeap = [-(x+1001) for x in nums] #deep copy + *-1
        heapq.heapify(minHeap)
        for i in range(k-1):
            #pop k times
            heapq.heappop(minHeap)
        return (-minHeap[0])-1001


        