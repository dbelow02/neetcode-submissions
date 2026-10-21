class MinStack:
#This is fun. Feels like DSA again.
    def __init__(self):
        #Just a regular list stack an extra int for min
        #Assumes "retrieves does not mean remove"
        #If remove, keep index.
        #keep first 
        self.stack = []
        #keep track of what the min is at each point of insertion
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) > 0:
            self.mins.append(min(self.mins[-1], val))
        else:
            self.mins.append(val)
        
    def pop(self) -> None:
        #What if elt is the min?
        #how do we repop minElt in O(1)?
        self.stack.pop()
        self.mins.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
