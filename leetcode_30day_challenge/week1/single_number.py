class Solution:
    def singleNumber(self, nums) -> int:
        hash_table = {}
        for val in nums:
            try:
                hash_table[val] += 1
            except:
                hash_table[val] = 1
        for key, val in hash_table.items():
            if val == 1:
                return key

print(Solution().singleNumber([2,2,1]))