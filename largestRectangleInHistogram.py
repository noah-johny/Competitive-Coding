class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = heights[0]
        stack = []

        for i, h in enumerate(heights):
            index = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))

            stack.append((index, h))

        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))

        return maxArea