class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_prod = [1] * n
        r_prod = [1] * n

        prod = 1
        for i in range(0, len(nums), 1):
            prod *= nums[i]
            l_prod[i] = prod
        
        prod = 1
        for i in range(len(nums) -1, -1, -1):
            prod *= nums[i]
            r_prod[i] = prod
        
        result = []
        for i in range(0, len(nums), 1):
            l = l_prod[i-1] if i > 0 else 1
            r = r_prod[i+1] if i < n-1 else 1
            result.append(l * r)

        return result

