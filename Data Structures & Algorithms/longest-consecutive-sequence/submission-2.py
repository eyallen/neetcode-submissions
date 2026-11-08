class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            if num - 1 in seen:
                continue
            end = num
            while end + 1 in seen:
                end += 1
            longest = max(longest, end - num + 1)
        return longest