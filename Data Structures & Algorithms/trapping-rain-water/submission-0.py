class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
        result = 0

        while l < r:
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)
            if height[l] < height[r]:
                result += maxL - height[l]
                l += 1
            else:
                result += maxR - height[r]
                r -= 1

        return result