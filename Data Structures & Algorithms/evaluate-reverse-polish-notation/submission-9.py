class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #First of all, what the heck is RPN..
        #Seems like another language to me.

        #How do we handle parenthesis?
        #Evaluate the first tokens first I guess..

        #Trick is keeping track of current sum in the stack as well!
        numstack = []
        for token in tokens:
            if token in ["+","-","*","/"]:
                #Do the math!
                #Grab 2 recent entries
                right = numstack.pop()
                left = numstack.pop()
                num = 0
                if token == "+":
                    num = left + right
                elif token == "-":
                    num = left - right
                elif token == "*":
                    num = left * right
                elif token == "/":
                    num = int(left / right) # needs to be int(x/y) instead of x // y because truncate towards 0 is not floor if result is negative.
                #Add to the stack for future processing!
                numstack.append(num)
            else:
                #Must be a num. Add it to the stack to be processed later.
                numstack.append(int(token))
        return numstack.pop()
            