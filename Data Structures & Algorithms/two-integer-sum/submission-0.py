class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = dict()

        # build a dict of indicies of a given number
        for i, n in enumerate(nums):
            num_index.setdefault(n, [])
            num_index[n].append(i)

        # then loop through values and find if target-curr exists
        for i, n in enumerate(nums):
            to_find = target - n

            if to_find in num_index:
                # We need to check its not the current index
                for j in num_index[to_find]:
                    if j != i:
                        return [i, j]
        
        return[0,0]

        