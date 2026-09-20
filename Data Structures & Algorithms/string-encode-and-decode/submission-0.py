class Solution:
    #Main challenge will be distinguishing against things like:
    #["string1", "string2"]
    #and
    #["string1string2"]
    #Need to join by some unique character.
    #strings contains any of 256 valid ASCII characters.
    #At most 100 strings, with each string being at most 199 chars long

    #Two approaches, join each string with a char that doesn't exist elsewhere.
    #Pad information about the compression of string at end of max possible string.
    #What about joining by string length?
    def encode(self, strs: List[str]) -> str:
        out = []
        for word in strs:
            word = str(len(word)) + "#" + word
            out.append(word)
        return "".join(out)
            #word = "word"
            #4#word
    def decode(self, s: str) -> List[str]:
        words = []
        wordlen = None
        #2 phases:
        #Get length
        #Get word
        i = 0
        while i < len(s):
            #Get wordlen
            lenstring = ""
            while s[i] != "#":
                lenstring += s[i]
                i += 1
            wordlen = int(lenstring)
            words.append(s[i+1:i+wordlen+1])
            i = i+wordlen+1
        return words



