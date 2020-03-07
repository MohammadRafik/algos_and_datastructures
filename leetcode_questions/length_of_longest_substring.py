# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s) -> int:
    length_of_sub_strings = []
    for i in range(len(s)):
        finding_substring = True
        j = i
        hash_table = {}
        hash_table[s[j]] = 1
        while(j < len(s)-1):
            j += 1
            if s[j] in hash_table:
                    break
            else:
                hash_table[s[j]] = 1
        length_of_sub_strings.append(len(hash_table))
    return max(length_of_sub_strings )

print(lengthOfLongestSubstring('abcdefaafsdxa'))