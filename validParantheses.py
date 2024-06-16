class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '(': ')', '[': ']'}
        stack = []

        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif not stack or brackets[stack.pop()] != ch:
                return False

        return not stack