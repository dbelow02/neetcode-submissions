class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Choose any of the letters digit represents
        #Continue until done with digits
        #Then append and backtrack
        #Could also index alphabet based on digit.. but
        digittoletter = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        combinations = []

        def dfs(curstring, index):
            if index >= len(digits):
                if len(curstring) > 0:
                    combinations.append(curstring)
                return
            for c in digittoletter[digits[index]]:
                curstring += c
                dfs(curstring, index+1)
                curstring = curstring[:-1]
            return

        dfs("", 0)
        return combinations