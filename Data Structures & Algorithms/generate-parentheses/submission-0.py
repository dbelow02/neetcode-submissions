class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Backtracking
        #Choice is we either close a parentheses or we leave it open
        result = []

        def dfs(numleft, curstring, openparenthesis):
            #if num left is 0, close everything!
            if numleft == 0:
                for i in range(openparenthesis):
                    curstring += ")"
                result.append(curstring) #may need to deepcopy?
                return
            #We put in an open parenthesis
            curstring += "("
            dfs(numleft-1, curstring, openparenthesis+1)
            curstring = curstring[:-1]
            if openparenthesis > 0:
                curstring += ")"
                dfs(numleft, curstring, openparenthesis-1)
                #We put in a closed pair
            return
        
        dfs(n, "", 0)
        return result

        #Currently have a problem at n = 1 we end up with ["()","()"]
            