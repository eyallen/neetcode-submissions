class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        product = 1
        ltr = [1] * n
        for i in range(0, len(nums)):
            product *= nums[i]
            ltr[i] = product
        
        product = 1
        rtl = [1] * n
        for i in range(n-1, -1, -1):
            product *= nums[i]
            rtl[i] = product
        
        for i in range(0, len(nums)):
            l = ltr[i-1] if i-1 >= 0 else 1
            r = rtl[i+1] if i+1 <= len(nums)-1 else 1

            res[i] = l*r
        
        return res


