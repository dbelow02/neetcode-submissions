class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #O(n) time, O(m) space. N is len of string, m is num unique chars.
        #Not sure I fully understand constraint
        #Would yabaybc
        #Find longest substring at each unique character is strat
        #How can we do this in a smart way other than check at each char?
        #Naive would be loop over string, get max substring at each string, then find longest substring from some dict
        #This is time O(N^2) and Space O(M) though.
        #Can we create a prefix/suffix structure?
        #character either starts a substring or is part of a substring.
        #Prefix/suffix list where list[i] is set for O(1) lookup?
        #Can potentially iterate up from 1 to find longest substring?

        #Use two pointers, left/right. Expand right until find duplicate in our existing set, then iterate left and update set. Max len of set throughout the slide is max len of substring.
        if len(s) < 2:
            return len(s)
        #s atleast len 2
        left = 0
        right = 1
        activeset = set()
        activeset.add(s[left])
        maxsize = len(activeset)
        while right <= len(s) - 1:
            if left == right: #left and right ==, restart hunt from new pos
                right += 1
                activeset = set(s[left])
            elif s[right] in activeset: #substring cannot grow from here.
                #Iterate left until right == left OR s[left] == s[right]
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        #also need to increment right here otherwise double checks
                        if right < len(s) - 1:
                            right += 1
                        else:
                            return(maxsize) #can only shrink
                        break
                    else:
                        activeset.remove(s[left])
                        left += 1
            else:
                activeset.add(s[right])
                right += 1
                if len(activeset) > maxsize:
                    maxsize = len(activeset)
        return maxsize
