class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        #Doubly linked list for tracking usage O(1) 
        #Hash for grabbing keys
        self.maxlen = capacity
        self.mru = None
        self.lru = None
        self.findNode = {}

    def get(self, key: int) -> int:
        #Set mru
        #Need to handle cases when mru and lru are None
        if key not in self.findNode:
            return -1

        node = self.findNode[key]
        if self.mru == node.key:
            #No change needed!
            return node.val
        else:
            #Adjust node pointers and LRUCache mru
            if node.prev:
                #Skip me because I'm moving!
                node.prev.next = node.next
            #No previous node
            if node.next:
                #Skip me, I'm moving!
                node.next.prev = node.prev
        if self.lru == node.key:
            #Swap lru out!
            self.lru = node.prev.key
        #new mru
        self.findNode[self.mru].prev = node
        node.next = self.findNode[self.mru]
        node.prev = None
        self.mru = node.key
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.findNode:
            node = self.findNode[key]
            node.val = value
            if self.mru != node.key:
                #Don't need to do anything if already mru
                if self.lru == node.key:
                    self.lru = node.prev.key
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                self.findNode[self.mru].prev = node
                node.next = self.findNode[self.mru]
                node.prev = None
                self.mru = node.key
        else:
            if len(self.findNode) != 0:
                #Normal case
                newNode = Node(key, value)
                newNode.next = self.findNode[self.mru]
                self.findNode[self.mru].prev = newNode
                self.mru = newNode.key
                self.findNode[key] = newNode
            else:
                #Init case
                newNode = Node(key, value)
                self.mru = newNode.key
                self.lru = newNode.key
                self.findNode[key] = newNode
        if len(self.findNode) > self.maxlen:
            #Need to evict something!
            newlru = self.findNode[self.lru].prev
            newlru.next = None
            del self.findNode[self.lru]
            self.lru = newlru.key

