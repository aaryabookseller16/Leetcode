class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        # iterate through the string 
        for c in s:
            # if opening bracket then push to stack
            if c in mapping.values():
                stack.append(c)
            
            # else: if its a closing bracket
            elif c in mapping:
                # if stack is empty or brackets dont match -> False
                if not stack or stack[-1] != mapping[c]:
                    return False
                # else pop
                else:
                    stack.pop()

            # else -> False
            else: 
                False

        # return
        return not stack