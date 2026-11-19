"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
#A naive, BAD solution based on space would be to use a set
#Increment from start to finish of meeting and check if in set already
#If not, add to set
#Return true if no elts already in set, otherwise false
#This also assumes integer values
#Could also sort based on first time in pair
#Then check if last time of pair > next start time
        sortedIntervals = sorted(intervals, key = lambda i: (i.start, i.end))
        for i in range(len(sortedIntervals)-1):
            if sortedIntervals[i].end > sortedIntervals[i+1].start:
                return False
        return True