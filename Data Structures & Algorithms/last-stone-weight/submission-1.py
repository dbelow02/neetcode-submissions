class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Heaviest stones first (max heap)
        #pop 2, compare, then either insert or continue
        invertedstones = [-x for x in stones]
        heapq.heapify(invertedstones)
        while len(invertedstones) >= 2:
            x = heapq.heappop(invertedstones)
            y = heapq.heappop(invertedstones)
            if x == y:
                continue
            else:
                heapq.heappush(invertedstones, -abs(x-y))
        if len(invertedstones) == 0:
            return 0
        return -invertedstones[0]
            