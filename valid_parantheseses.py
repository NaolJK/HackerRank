class Solution:
    def isValid(self, s: str) -> bool:
        all_endings = {
            '(':')',
            '{':'}',
            '[':']', 
        }
        
        stack = []
        
        for character in s:
            if character == "(" or character == "[" or character =='{':
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                if character != all_endings[stack.pop()]:
                    return False
        
        if len(stack) > 0:
            return False
                
        return True