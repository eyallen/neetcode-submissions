class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        seq_start = []

        for num in nums:
            if num-1 not in seen:
                seq_start.append(num)

        longest = 0
        for num in seq_start:
            target = num
            seq_len = 0
            while target in seen:
                target += 1
                seq_len += 1
            
            if seq_len > longest:
                longest = seq_len

        return longest