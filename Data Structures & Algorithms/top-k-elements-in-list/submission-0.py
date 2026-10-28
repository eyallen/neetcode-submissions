class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        # create a map of nums to frequency
        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
    
        arr = []
        for num, count in num_count.items():
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res