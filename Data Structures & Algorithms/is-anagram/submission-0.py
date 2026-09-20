class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Can't use sets for this one, need to count
        #The number of times a letter appears. Cut and dry dict()
        left = {}
        right = {}
        for character in s:
            if character in left.keys():
                left[character] += 1
            else:
                left[character] = 1

        for character in t:
            if character in right.keys():
                right[character] += 1
            else:
                right[character] = 1
        
        return left == right