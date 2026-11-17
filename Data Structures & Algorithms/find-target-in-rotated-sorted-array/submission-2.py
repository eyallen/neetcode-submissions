class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # find the pivot
        l, r = 0, n-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l

        # now find the part the number is in
        if nums[pivot] <= target <= nums[-1]:
            l, r = pivot, n
        else:
            l, r = 0, pivot

        while l < r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return -1