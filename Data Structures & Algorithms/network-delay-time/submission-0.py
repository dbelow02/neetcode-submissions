class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Do received nodes gossip to other nodes?
        #Or is it just waiting from a received node until all others
        #Note, jumped randomly to this question so unaware of 
        #General theme.
        #Think this is likely a dfs? Depends on if other talk
        #Wait its just a djikstras graph search
        #O(ElogV) time O(V+E) space
        #Lowkey don't remember Djikstras, good refresher!
        #Is it priority queue based?
        dists = [float('inf')] * n
        #Now, make the adjacency graph!
        adjacencyDict = defaultdict(list)#dict[node] = [(node, time)]
        for time in times:
            adjacencyDict[time[0]].append((time[1], time[2]))
        #We start at k
        priorityQ = [(0,k)]
        while len(priorityQ) > 0:
            dist, node = heapq.heappop(priorityQ)
            if dists[node-1] != float('inf'):
                continue
                #Already finalized on a shorter path
            else:
                dists[node-1] = dist
            for neighbor in adjacencyDict[node]:
                totaltime = neighbor[1] + dist
                heapq.heappush(priorityQ, (totaltime, neighbor[0]))
        out = max(dists)
        if out == float('inf'):
            return -1
        return out
