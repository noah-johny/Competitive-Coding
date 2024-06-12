class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)

        if size < 3:
            return 0
        
        left = [0] * size
        right = [0] * size
        
        left[0] = height[0]
        for i in range(1, size):
            left[i] = max(left[i-1], height[i])
        
        right[size-1] = height[size-1]
        for i in range(size-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        trappedWater = 0
        for i in range(size):
            trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater    