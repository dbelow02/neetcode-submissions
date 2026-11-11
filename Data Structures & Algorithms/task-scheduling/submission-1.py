class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Identical tasks must be separated by at least n. CPU cycles
        #Priority queue problem, but might be confused
        #Give priority to tasks with duplicates.
        #Keep a list of last n tasks
        #Check if priority queue pop in set? if not, increment
        #If yes, increment until empty or find elt not in set
        #Repopulate heap with commands that aren't executed
        #Because of delays
        #Keep counter for num cycles
        #Priority = num duplicates within queue?
        #use max heap (more counts = needs to be done first)
        counter = 0
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] -= 1
        #Now, heapify with (count, index), but filter out the 0's
        pairs = [(count, i) for i, count in enumerate(counts) if count != 0]
        heapq.heapify(pairs)
        lastn = deque([None] * n)
        queued = 0  #number of non-None entries in lastn
        while ((queued > 0) or (len(pairs) > 0)):
            counter += 1
            #lastn either has something queued, or pairs still full
            last = None
            if len(pairs) > 0:
                task = heapq.heappop(pairs)
                if(task[0] < -1):
                    #only append when it is NOT the last time
                    last = (task[0]+1, task[1])
            #If lastn[0] not None, add back in
            lastn.append(last)
            if last is not None:
                queued += 1
            last = lastn.popleft()
            if last is not None:
                queued -= 1
                heapq.heappush(pairs, last)
        return counter

        