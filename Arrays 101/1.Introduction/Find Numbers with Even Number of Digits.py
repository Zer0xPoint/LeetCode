class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_nums_count = 0
        for num in nums:
            local_count = 0
            while num > 0:
                num //= 10
                local_count += 1
            if local_count % 2 == 0:
                even_nums_count += 1
        return even_nums_count