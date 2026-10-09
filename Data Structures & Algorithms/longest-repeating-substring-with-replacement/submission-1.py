class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #This time, follow the prompt lol
        #Essentially a basic substring problem but deconflicting is different
        if len(s) - k <= 1:
            #early exit for trivial solves
            return len(s)
        letters = {}
        maxlen = 1
        #Choose which letter is our "base" letter via the dict
        #Whichever letter minimizes the number of wildcards needed
        left = 0
        #Need to balance dict at each step. (what letter are we running with)
        #If we can balance, great. Otherwise, deconflict
        #what is our max elt in the dict?
        letters[s[left]] = 1
        maxletter = s[left]
        for right in range(1,len(s)):
            if s[right] == maxletter:
                letters[s[right]] += 1
                if right - left + 1 > maxlen:
                    maxlen = right - left + 1
                #Do nothing, grow right further.
            else:
                #right not max letter, need use wildcard.
                num = letters.get(s[right], 0) + 1
                letters[s[right]] = num
                if letters[s[right]] > letters[maxletter]:
                    maxletter = s[right]
                if (right - left + 1) - letters[maxletter] <= k:
                    #We still have space for wildcards!
                    #Increment.
                    if right - left + 1 > maxlen:
                        maxlen = right - left + 1
                else:
                    #No space with wildcards, need to free one up!
                    while (right - left + 1) - letters[maxletter] > k:
                        letters[s[left]] -= 1
                        left += 1
                        maxletter = max(letters, key=letters.get)
        return maxlen