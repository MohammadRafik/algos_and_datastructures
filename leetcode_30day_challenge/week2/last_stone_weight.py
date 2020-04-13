class Solution:
    def lastStoneWeight(self, stones) -> int:
        stones = sorted(stones)[::-1]
        i = 0
        while 1 < len(stones):
            if stones[i] == stones[i+1]:
                stones.pop(i)
                stones.pop(i)
                continue
            if stones[i] < stones[i+1]:
                stones[i+1] -= stones[i]
                stones.pop(i)
                stones = sorted(stones)[::-1]
                continue
            else:
                stones[i] -= stones[i+1]
                stones.pop(i+1)
                stones = sorted(stones)[::-1]
                continue
        if stones:
            return stones[0]
        else:
            return 0




print(Solution().lastStoneWeight([2,7,4,1,8,1]))