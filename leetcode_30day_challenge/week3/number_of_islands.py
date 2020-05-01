class Solution:
    def numIslands(self, grid) -> int:
        if grid == []:
            return 0
        grid_len = len(grid)
        inner_len = len(grid[0])

        checked_values = [['e' for i in range(inner_len)] for j in range(grid_len)]
        
        island_count = 0

        def permeate_and_set(grid, checked_values, i, j):
            # evaluate current index
            if checked_values[i][j] == 'e' and grid[i][j] == '1':
                checked_values[i][j] = '1'
            else:
                return
            
            # permeate
            try:
                if 0 < j:
                    permeate_and_set(grid,checked_values,i ,j-1)
            except:
                pass
            try:
                permeate_and_set(grid,checked_values,i ,j+1)
            except:
                pass
            try:
                
                if 0 < i:
                    permeate_and_set(grid,checked_values,i-1 ,j)
            except:
                pass
            try:
                permeate_and_set(grid,checked_values,i+1 ,j)
            except:
                pass


        for i in range(grid_len):
            for j in range(inner_len):
                if checked_values[i][j] == 'e':
                    if grid[i][j] == "1":
                        island_count += 1
                        permeate_and_set(grid, checked_values, i, j)
        return island_count


x = Solution().numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]])
print(x)


