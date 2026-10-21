class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()

        # build a dict of indicies of a given number
        for i, n in enumerate(nums):
            num_index[n] = i

        # then loop through values and find if target-curr exists
        for i, n in enumerate(nums):
            to_find = target - n

            if to_find in num_index and num_index[to_find] != i:
                return [i, num_index[to_find]]
        
        return[0,0]