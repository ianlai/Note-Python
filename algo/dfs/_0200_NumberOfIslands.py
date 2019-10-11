class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 :
            return 0
        count = 0
        print("row:", len(grid), " col:", len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(grid[i][j], end="")
                if grid[i][j] == "1":
                    count += 1
                    self.foundIsland(grid, i,j)
            #print()
        return count
                    
    def foundIsland(self, grid, i, j):
        if i < 0 or i >= len(grid):
            return 
        if j < 0 or j >= len(grid[0]):
            return 
        if grid[i][j] == "0":
            return 
        elif grid[i][j] == "1":
            grid[i][j] = "0"
            self.foundIsland(grid, i-1, j)
            self.foundIsland(grid, i+1, j)
            self.foundIsland(grid, i, j-1)
            self.foundIsland(grid, i, j+1)
        