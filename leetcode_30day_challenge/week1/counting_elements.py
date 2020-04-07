class Solution:
    def countElements(self, arr) -> int:
        hash_table = {}

        for i in range(len(arr)):
            if arr[i] in hash_table:
                hash_table[arr[i]] += 1
            else:
                hash_table[arr[i]] = 1
        
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in hash_table:
                count += 1
        return count



print(Solution().countElements([]))