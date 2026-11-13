class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Choice is which index to partition on
        #Can partition until len s = 1
        palindromes = []

        def dfs(curString, curPartitions):
            if len(curString) == 0:
                # nothing left: every piece we chose was a palindrome
                palindromes.append(list(curPartitions))
                return
            for i in range(1, len(curString) + 1):
                piece = curString[:i]          # first piece = first i chars
                #Choose partition!
                #If partition is palindrome, continue down on leftovers
                if self.isPalindrome(piece):
                    curPartitions.append(piece)
                    dfs(curString[i:], curPartitions)  # partition the rest
                    curPartitions.pop()

        dfs(s, [])
        return palindromes

        
    



    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while right > left:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True