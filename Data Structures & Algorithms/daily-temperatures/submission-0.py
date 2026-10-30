class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Ah, interesting problem
        #If I didn't know better I might try a pointer approach
        #Sliding window or two pointer problem is intuitive
        #But, likely a stack problem.
        #Or could lowkey be a priority queue

        #Start from end?
        #O(n) time and space
        #Can make a stack, two stacks?
        # [2,1,1,3]
        #From 3, none can be greater
        #From 1 only 3 can be, is it?
        
        #Iterate from end of list, creating stack with each popped elt
        #How can we use < or > to help us here?
        
        out = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[i-1]:
                stack.append(i)
                continue
            #Temp is not less than less temp, pop stack until one is larger
             #we know this first elt is < temp[i]
            elt = stack[-1]
            while temperatures[elt] < temperatures[i]:
                stack.pop()
                out[elt] = i - elt
                if len(stack) == 0:
                    break
                elt = stack[-1]
            stack.append(i)
        #Reached the end, there are no greater temps.
        return out

            

