class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mapping:
                top = stack.pop() if stack else '#'
                if mapping[ch] != top:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0