class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_sort = sorted(nums)

        idx = {}
        for i, v in enumerate(num_sort):
            idx[v] = i
        
        found = set()
        for i in range(len(num_sort)):
            for j in range(i+1, len(num_sort)):
                x = -(num_sort[i] + num_sort[j])
                if x in idx and idx[x] > j:
                    found.add(tuple((num_sort[i], num_sort[j], x)))
        
        return [list(t) for t in found]