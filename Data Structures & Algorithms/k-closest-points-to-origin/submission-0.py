class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Calculate distance on each, then minheap?
        #Need to keep index with distance - tuple?
        #Python heap evaluates tuples by first elt, then second.
        #Fine in this case given unique solution
        #nlogk
        distances = [(self.getDist(pair), i) for i, pair in enumerate(points)]
        heapq.heapify(distances)
        out = []
        for i in range(k):
            smallest = heapq.heappop(distances)
            out.append(points[smallest[1]])
        return out
    def getDist(self, pair):
        return ((pair[0]**2) + (pair[1]**2)) ** 1/2