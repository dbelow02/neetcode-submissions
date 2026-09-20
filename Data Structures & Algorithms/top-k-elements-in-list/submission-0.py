class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most frequent integers in nums
        #output in any order
        #k <= distinct ints in nums
        
        #Map ints to frequency in dict
        #Then put into max heap / priority queue?
        numbers = {}
        for num in nums:
            cur_count = numbers.get(num)
            if cur_count is None:
                numbers[num] = 1
            else:
                numbers[num] += 1
        #Now, have dict of int -> count.
        #Get list of (int, count)
        pairs = list(numbers.items())
        #Now, put pairs into max heap sorted by pairs[i]
        #Heap sorts tuples based on index. Flip [0] and [1]
        heap = []
        for pair in pairs:
            #-count to make max heap
            heapq.heappush(heap, (-pair[1], pair[0]))
        out = []
        for i in range(k):
            pair = heapq.heappop(heap)
            out.append(pair[1])
        #Now, pop k elements from heap.
        return out
