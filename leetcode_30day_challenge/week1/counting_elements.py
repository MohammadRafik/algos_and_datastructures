class Solution:
    def countElements(self, arr) -> int:
        
        hash_table = {}
        for i in range(len(arr)):
            if arr[i] not in hash_table:
                hash_table[arr[i]] = True
        
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in hash_table:
                count += 1
        return count



print(Solution().countElements([1,1,2]))