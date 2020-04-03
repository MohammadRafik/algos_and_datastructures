class Solution:
    def isHappy(self, n) -> bool:
        processed_values = []
        while n != 1:
            str_n = str(n)
            if n not in processed_values:
                processed_values.append(n)
                new_n = 0
                for ele in str_n:
                    new_n += int(ele)**2
            else:
                return False
            n = new_n
        return True

Solution().isHappy(22)