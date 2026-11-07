class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # first, find the inflection point
        l, r = 0, n-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        # find the half that can hold the target
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, n
        else:
            l, r = 0, pivot
        
        while l < r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid
        
        return -1

            
