class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left, right = 0, size-1
        area = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] * (right-left) > area:
                    area = height[left] * (right-left)
                left += 1
            else:
                if height[right] * (right-left) > area:
                    area = height[right] * (right-left)
                right -= 1
            
        return area