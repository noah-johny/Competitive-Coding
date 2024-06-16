class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for token in tokens:
            if token in "+-*/" and len(stack) >= 2:
                n2 = stack.pop()
                n1 = stack.pop()

                if token == "+":
                    res = n1 + n2
                elif token == "-":
                    res = n1 - n2
                elif token == "*":
                    res = n1 * n2
                elif token == "/":
                    res = n1 / n2

                stack.append(int(res))
            else:
                stack.append(int(token))

        if not stack:
            return res
        else:
            return stack.pop()