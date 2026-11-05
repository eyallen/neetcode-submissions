class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        idx = {}
        for i, v in enumerate(nums):
            idx[v] = i

        found = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                c = -(nums[i] + nums[j])
                if c in idx and idx[c] > j:
                    found.add(tuple(sorted((nums[i], nums[j], c))))
        return [list(t) for t in found]
                
