class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Pretty sure I got a similar question to this in an IBM OA
        #Yea.. this is the exact question. Actually, not. Larger elements had to be to the right, but not necessarily consecutive.
        #Collect values, then loop over.
        #best way to collect? Into a scaled array
        #index would be max/n bins.
        #Min max scale wouldn't work bc outliers mess up bins.
        #Can check if previous number already in set.
        if nums == []:
            return 0
        numbers = set(nums)
        starts = set()
        longest_set = 1
        for num in nums:
            if num-1 not in numbers:
                starts.add(num)
        #Now, check the longest start.
        for start in starts:
            length = 1
            i=1
            while True:
                if start + i in numbers:
                    length += 1
                    i += 1
                    if length > longest_set:
                        longest_set = length
                else:
                    break
        return longest_set