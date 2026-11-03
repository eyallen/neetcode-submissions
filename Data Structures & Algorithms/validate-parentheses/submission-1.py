class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        match_table = { ')' : '(', ']' : '[', '}' : '{'}

        for char in s:
            if char in match_table:
                # we have a closing paren
                if stack:
                    top = stack.pop()
                    if top != match_table[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0