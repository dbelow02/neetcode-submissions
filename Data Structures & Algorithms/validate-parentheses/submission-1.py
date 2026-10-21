class Solution:
    def isValid(self, s: str) -> bool:
        #Wait this is literally just a stack
        #Just use a list.
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for character in s:
            if character in ["(","{","["]:
                #append
                stack.append(character)
            elif character in [")","}","]"]:
                if len(stack) == 0 or stack.pop() != pairs[character]:
                    return False
        return len(stack) == 0

        