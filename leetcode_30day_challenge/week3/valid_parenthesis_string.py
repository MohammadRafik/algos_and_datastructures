class Solution:
    def checkValidString(self, s: str) -> bool:
        len_s = len(s)
        positions = [None] * len_s

        for i in range(len_s):
            if s[i] == '(':
                positions[i] = '('

            elif s[i] == ')':
                found = False
                for j in range(len(positions)-1,-1,-1):
                    if positions[j] == '(':
                        positions[j] = None
                        found = True
                        break
                if not found:
                    for j in range(len(positions)):
                        if positions[j] == '*':
                            positions[j] = None
                            found = True
                            break
                if not found:
                    return False
            else:
                positions[i] = '*'

        for i in range(len(positions)):
            if positions[i] == '(':
                j = i
                for x in range(j,len(positions)):
                    if positions[x] == '*':
                        positions[x] = None
                        positions[i] = None
                        break
        
        for val in positions:
            if val == '(':
                return False
        return True



            

print(Solution().checkValidString('()'))
                             