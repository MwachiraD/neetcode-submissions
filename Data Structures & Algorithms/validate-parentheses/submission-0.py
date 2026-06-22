class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
           ')':'(', 
           '}':'{',
           ']':'['
        }
        stack = []
        for char in s:
            if char in mappings:
                if not stack:
                    return False
                top = stack.pop()

                if top != mappings[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
            



                
        