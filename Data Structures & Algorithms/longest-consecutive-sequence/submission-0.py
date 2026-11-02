class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()

        for num in nums:
            hs.add(num)
        
        seq_start = set()
        for num in nums:
            if num-1 not in hs:
                seq_start.add(num)
        
        max_len = 0
        for s in seq_start:
            seq_len = 1
            to_find = s+1

            while to_find in hs:
                seq_len += 1
                to_find += 1
            
            if seq_len > max_len:
                max_len = seq_len
        
        return max_len

            
