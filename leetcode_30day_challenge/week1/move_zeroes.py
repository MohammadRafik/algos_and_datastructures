class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes_que = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes_que.append(i)
            elif zeroes_que:
                nums[zeroes_que.pop(0)] = nums[i]
                nums[i] = 0
                zeroes_que.append(i)


ary = [3,0,22,0,0,0,42,2342134,0,0,1,2,3,4,0,0,32,0,123,0,1231,0,0,12,1234,0,0,0,23232,212]
print(ary)
Solution().moveZeroes(ary)
print(ary)