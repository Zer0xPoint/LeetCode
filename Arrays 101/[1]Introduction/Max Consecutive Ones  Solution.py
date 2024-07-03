class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        max_local = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                max_local += 1
                max_consecutive = max(max_local, max_consecutive)
            else:
                max_local = 0
        return max_consecutive