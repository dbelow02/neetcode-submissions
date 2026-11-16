"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #This is similar to an island search
        #Iterate through all nodes
        #Keep track of which ones have already done
        #Hash old node to new node
        #Queue for bfs
        #Try to map neighbors as we go.
        #If can't figure it out, could do a second pass for assigning neighbors
        
        if node is None:
            return
        originalNode = node
        oldtonew = {}
        queue = deque()
        queue.append(node)
        while len(queue) > 0:
            oldnode = queue.popleft()
            if oldnode not in oldtonew:
                newNode = Node(val=oldnode.val)
                oldtonew[oldnode] = newNode
            else:
                newNode = oldtonew[oldnode]
            for neighbor in oldnode.neighbors:
                if neighbor not in oldtonew:
                    newNeighbor = Node(val=neighbor.val)
                    oldtonew[neighbor] = newNeighbor
                    queue.append(neighbor)
                newNode.neighbors.append(oldtonew[neighbor])
        return oldtonew[originalNode]

