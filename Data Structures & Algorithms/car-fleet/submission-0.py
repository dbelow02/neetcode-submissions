class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #goal is destination, all cars going there
        #cars cannot pass each other
        #They can catch up to each other and then drive together.
        #This means they came have the same position and same speed
        #The question is how many fleets arrive at the detination
        #A fleet can be 1 car, or many.

        #Don't need to keep track of the number of cars in a fleet.
        #Just keep track if it'll catch it
        #Can merge fleets this way.

        #Can check if will catch up to car in front
        #However, array is not sorted 

        #What if instead of counting cars, count steps towards target?
        #Want O(nlogn) time and O(n) space.
        #This means, could sort...
        #Sort by position, then stack by speed?

        #However, will need to keep track of indices for speed.
        #If a car is ahead, and going faster, it cannot form a fleet.
        sortedPositions = sorted(enumerate(position), key=lambda x: x[1], reverse=True)
        #Cars closest to target returned first
        curSlowest = (target - sortedPositions[0][1]) / speed[sortedPositions[0][0]]
        fleets = 1
        for i in range(1, len(position)):
            #If can't be part of a new fleet, append
            #Can't be part of new fleet if expected arrival <= car ahead of you
            #Only add cars that might be part of a new fleet to stack
            timetodestbehind = (target - sortedPositions[i][1]) / speed[sortedPositions[i][0]]
            if timetodestbehind <= curSlowest:
                continue
            #Otherwise, this car can potentially start a new fleet
            #Or, it might not, depending on traffic ahead.
            fleets += 1
            curSlowest = timetodestbehind
            #How do we decide if it does?
            #Starts a new fleet when it can't reach ANY of the cars ahead of it.
            #So, just need to keep track of the slowest car 
        return fleets


        