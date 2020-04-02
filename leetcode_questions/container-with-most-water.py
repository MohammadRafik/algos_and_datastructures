class Solution:
    def maxArea(self, height) -> int:
        vals = []
        i = 0
        j = len(height) - 1
        while i <= j:
            vals.append(min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max(vals)


Solution().maxArea([1,2,3,4,5,6,7,8])


