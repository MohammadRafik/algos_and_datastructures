class Solution:
    def productExceptSelf(self, nums):
        sum = 1
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter += 1
            else:
                sum *= num
        if 1 < zero_counter:
            return [0] * len(nums)
        if 1 == zero_counter:
            products = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    products[i] = sum
                else:
                    products[i] = 0
            return products

        products = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                products[i] = 0
            else:
                products[i] = int(sum / nums[i])
        return products


print(Solution().productExceptSelf([1,0]))