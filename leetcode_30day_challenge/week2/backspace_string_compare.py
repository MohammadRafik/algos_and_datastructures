class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def filter(S: str):
            filtered = []
            for s in S:
                if s != '#':
                    filtered.append(s)
                elif filtered:
                    filtered.pop()
            return filtered
                    

        if filter(S) == filter(T):
            return True
        else:
            return False

print(Solution().backspaceCompare('a###################aa##D', "acc##D"))