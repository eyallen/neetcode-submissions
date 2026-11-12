class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = {}

        for i,n in enumerate(nums):
            to_find = target - n
            if to_find in index_list and index_list[to_find] != i:
                return [index_list[to_find], i]

            index_list[n] = i
                
        return []
        