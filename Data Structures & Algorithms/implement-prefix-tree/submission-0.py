class PrefixTree:
    #O(n) time for each function, O(t) space. N is length of string
    #t is nodes created in Trie
    #What is the smart datastructure?
    #Tree structure with hashing at each node?

    def __init__(self):
        #Could make this all O(1) with an HTable similar to Cassandra
        #However, creates false positives.
        self.childHash = {} #char -> prefixTree object
        self.lastChar = False
        

    def insert(self, word: str) -> None:
        #Iterate through tree, create new nodes where needed.
        curHash = self.childHash
        for i, c in enumerate(word):
            if c in curHash:
                #Node already exists, traverse
                if i == len(word)-1:
                    curHash[c].lastChar = True
                curHash = curHash[c].childHash
            else:
                #Node does not exist, create one
                newNode = PrefixTree()
                if i == len(word)-1:
                    #last char in word
                    newNode.lastChar = True
                curHash[c] = newNode
                curHash = curHash[c].childHash
        return


    def search(self, word: str) -> bool:
        #Search and startsWith can be essentially the same
        #One is just on a prefix and the other is the whole word
        #... Just a longer "prefix"
        #May need to check if last char?
        curHash = self.childHash
        for i, c in enumerate(word):
            if c in curHash:
                #Continue looking
                if i == len(word) - 1:
                    if curHash[c].lastChar == True:
                        return True
                    else:
                        return False
                curHash = curHash[c].childHash
            else:
                #Nope!
                return False
        #Found all the chars
        return True

        

    def startsWith(self, prefix: str) -> bool:
        curHash = self.childHash
        for c in prefix:
            if c in curHash:
                #Continue looking
                curHash = curHash[c].childHash
            else:
                #Nope!
                return False
        #Found all the chars
        return True
        