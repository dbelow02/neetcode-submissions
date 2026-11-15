class WordDictionary:
    #Think this is similar to the prefix tree problem
    #"."s result in a recursive call/ traversal of ALL chars

    def __init__(self):
        self.childHash = {}
        self.endWord = False

    def addWord(self, word: str) -> None:
        curHash = self.childHash
        for i, c in enumerate(word):
            if c in curHash:
                #Already exists
                if i == len(word) - 1:
                    curHash[c].endWord = True
                curHash = curHash[c].childHash
            else:
                newNode = WordDictionary()
                if i == len(word) - 1:
                    newNode.endWord = True
                curHash[c] = newNode
                curHash = newNode.childHash
        return

    def search(self, word: str) -> bool:
        curHash = self.childHash
        for i, c in enumerate(word):
            if c == ".":
                #explore all letter paths
                for node in curHash:
                    if curHash[node].search(word[i+1:]):
                        return True
                return False
            else:
                if c in curHash:
                    if i == len(word) - 1:
                        return curHash[c].endWord
                    curHash = curHash[c].childHash
                else:
                    return False
        #Only reached when "." is the last char.
        return self.endWord
