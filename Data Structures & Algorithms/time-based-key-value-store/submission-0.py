class TimeMap:

    def __init__(self):
        #Idea would just be dict of word -> list of timestamps
        #Would need to be sorted
        #Fortunately, strictly increasing
        #Then, can binary search over timestamps
        #Get would be O(1)
        #Since timestamps strictly increasing, can get with O(logN)
        self.words = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        cur = self.words.get(key,[])
        cur.append((value,timestamp))
        self.words[key] = cur

    def get(self, key: str, timestamp: int) -> str:
        #Binary search over timestamps
        #If no values ""
        #Returns value at the largest timestamp <= timestamp
        values = self.words.get(key,[])
        if len(values) == 0:
            return ""
        low = 0
        high = len(values)
        while low != high:
            mid = (low + high) // 2
            if values[mid][1] > timestamp:
                high = mid
            else:
                low = mid + 1
        if values[low-1][1] <= timestamp:
            return values[low-1][0]
        return ""
