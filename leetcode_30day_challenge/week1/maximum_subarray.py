class Solution:
    def maxSubArray(self, nums) -> int:
        sub_array_sums = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            sub_array_sums.append(sum)
            if sum < 0:
                sum = 0
        return max(sub_array_sums)



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))