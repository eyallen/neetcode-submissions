class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()

        # build a dict of indicies of a given number
        for i, n in enumerate(nums):
            to_find = target - n
            
            if to_find in num_index:
                return [num_index[to_find], i]
            else:
                num_index[n] = i
        
        return[0,0]