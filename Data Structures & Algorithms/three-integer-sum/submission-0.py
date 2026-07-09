class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        i = 0
        while i < (len(nums) - 2):
            while i < (len(nums) - 2) and i > 0 and nums[i] == nums[i - 1]:
                i += 1
            target = (-1) * nums[i]
            l, r = i + 1, (len(nums) - 1)

            while l < r:
                curr = nums[r] + nums[l]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            i += 1
        return result
