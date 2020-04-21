class Solution:
    def stringShift(self, s: str, shift) -> str:
        final_shift = 0
        for one_shift in shift:
            if one_shift[0] == 0:
                final_shift -= one_shift[1]
            elif one_shift[0] == 1:
                final_shift += one_shift[1]

        swap = False
        if final_shift < 0:
            swap = True
            final_shift = final_shift * -1
        final_shift = final_shift%len(s)
        if swap:
            final_shift = final_shift * -1
                
        
        new_s = []
        for i in range(len(s)):
            shift_amount = (-final_shift + i)%len(s)
            new_s.append(s[shift_amount])
        a = ''
        return a.join(new_s)
            

print(Solution().stringShift("wpdhhcj", [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]))