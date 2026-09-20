class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #k most frequent integers in nums
        #output in any order
        #k <= distinct ints in nums
        
        #Map ints to frequency in dict
        #Then put into max heap / priority queue?
        #But, what if we can avoid sorting all together.
        #Put into array at index frequency, then iterate thru array
        numbers = {}
        for num in nums:
            cur_count = numbers.get(num)
            if cur_count is None:
                numbers[num] = 1
            else:
                numbers[num] += 1
        #Now, have dict of int -> count.

        #Put into list at index frequency, avoids sorting.
        frequencies = [None] * (len(nums) + 1)
        for num in numbers.keys():
            if frequencies[numbers[num]] == None:
                frequencies[numbers[num]] = [num]
            else:
                frequencies[numbers[num]].append(num)
        #Now, have list of none / numbers. Iterate from end to begin
        out = []
        i = len(nums)
        while len(out) < k:
            if frequencies[i] is None:
                i -= 1
            else:
                out.extend(frequencies[i])
                i -= 1
        return out
