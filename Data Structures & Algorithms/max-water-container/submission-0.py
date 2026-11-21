class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) -1

        while l < r:
            container_height = min(heights[l], heights[r])
            water_height = (r-l) * container_height

            max_water = max(max_water, water_height)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water