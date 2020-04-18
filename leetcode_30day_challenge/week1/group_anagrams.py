class Solution:
    def groupAnagrams(self, strs):
        dict = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in dict:
                dict[sorted_str].append(str)
            else:
                dict[sorted_str] = [str]

        return [dict[x] for x in dict]

strs = ["tea","and","ace","ad","eat","dans", '','',""]
print(Solution().groupAnagrams(strs))

