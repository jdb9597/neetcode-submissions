class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_result = 0
        while l < r:
            max_result = max(min(height[l],height[r]) * (r - l), max_result)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_result
        