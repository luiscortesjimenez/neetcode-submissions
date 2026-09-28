class Solution:
    def isValid(self, s: str) -> bool:
        # arr to be used as stack
        stack = []
        # map closing parenthesis to open
        close_to_open_map = {')':'(', ']':'[', '}':'{'}

        # loop thru all parenthesis
        for char in s:
            # if its a closing parenthesis
            if char in close_to_open_map:
                # if stack is nonempty and the top element
                # (inner open parenthesis) matches inner close pop
                if stack and stack[-1] == close_to_open_map[char]:
                    stack.pop()
                # if no match or no open parenthesis, false
                else:
                    return False
            # if its a open parenthesis add to stack
            else:
                stack.append(char)
        # if stack empty then Valid
        return len(stack) == 0