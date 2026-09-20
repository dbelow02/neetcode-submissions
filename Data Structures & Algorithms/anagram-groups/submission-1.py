class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Can just hash on letter frequency.
        #Ie. sort string, from racecar to aaccerr and hash. 
        #Then, return hash buckets

        #Takes NlogN time to sort a string though. What if instead, 
        #Assigned key value as an operation of string?
        #A -> 0, B->1, etc. However, need to be careful of collisions 
        #Just use an array
        anagrams = {}
        for word in strs:
            letters = [100] * 26 #needs to be 100 instead of 0 to avoid overflow to 10 causing incorrect binning.
            for letter in word:
                letters[ord(letter.lower()) - ord('a')] += 1
            #Turn the array into a string (so can be dict key)
            letters_key = "".join([str(num) for num in letters])
            anagrams.setdefault(letters_key, []).append(word)
        output = [anagrams[x] for x in anagrams.keys()]
        return output
        


        