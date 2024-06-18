class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i-index
            stack.append(i)

        return answer